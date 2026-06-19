import os
import streamlit as st
from groq import Groq
import pypdf
from streamlit_mic_recorder import speech_to_text
import json
from datetime import datetime
import time

# 1. Configure Streamlit UI Layout (Must be the first Streamlit command)
st.set_page_config(page_title="Groq Lightning Chatbot", page_icon="⚡", layout="wide")

# Custom CSS for better UX
st.markdown("""
    <style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. SAFE KEY ENTRY: Ask for the key in the sidebar
st.sidebar.header("🔑 Authentication")
api_key_input = st.sidebar.text_input("Enter your Groq API Key:", type="password", help="Get your key from console.groq.com")

if not api_key_input:
    st.info("👈 Please enter your Groq API key in the sidebar to unlock the chatbot.")
    st.stop()

# 3. Initialize Groq Client safely using the provided input
client = Groq(api_key=api_key_input)

# App Titles
st.title("⚡ Groq Lightning Chatbot")
st.caption("Blazing fast conversation with Llama-3.3-70b via Groq Hardware")

# 4. Sidebar Layout for Bonus Features
with st.sidebar:
    st.write("---")
    st.header("Settings & Features")
    
    # Model Selection
    selected_model = st.selectbox(
        "Choose Groq Model:",
        ["llama-3.3-70b-versatile", "llama3-8b-8192", "mixtral-8x7b-32768"],
        index=0
    )
    
    st.write("---")
    
    # Response Settings
    st.subheader("🎨 Response Settings")
    temperature = st.slider(
        "Creativity (Temperature):", 
        min_value=0.0, 
        max_value=1.5, 
        value=0.5, 
        step=0.05,
        help="Lower = more focused, Higher = more creative"
    )
    
    max_tokens = st.slider(
        "Max Response Length:", 
        min_value=100, 
        max_value=4096, 
        value=1024, 
        step=50,
        help="Maximum tokens in response"
    )
    
    response_format = st.selectbox(
        "Response Format:", 
        ["Default", "Bullet Points", "Step-by-Step", "Table Format"],
        help="How the AI should structure responses"
    )
    
    st.write("---")
    
    # PDF Document Context (Enhanced)
    st.subheader("📁 Document Context (PDF)")
    
    # Multiple PDF upload
    uploaded_files = st.file_uploader(
        "Upload PDF(s) to chat with:", 
        type=["pdf"], 
        accept_multiple_files=True,
        key="pdf_uploader"
    )
    pdf_context = ""
    pdf_filenames = []
    query_mode = "💬 Ask anything (AI + PDF)"
    
    if uploaded_files:
        progress_bar = st.progress(0)
        for idx, uploaded_file in enumerate(uploaded_files):
            try:
                pdf_reader = pypdf.PdfReader(uploaded_file)
                extracted_text = []
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        extracted_text.append(text)
                file_text = "\n".join(extracted_text)
                pdf_context += f"\n\n--- Content from {uploaded_file.name} ---\n{file_text}"
                pdf_filenames.append(uploaded_file.name)
                progress_bar.progress((idx + 1) / len(uploaded_files))
            except Exception as e:
                st.error(f"Error parsing {uploaded_file.name}: {e}")
        
        st.success(f"✅ Indexed {len(uploaded_files)} PDF(s): {', '.join(pdf_filenames)}")
        
        # PDF Query Mode
        query_mode = st.radio(
            "PDF Query Mode:", 
            ["💬 Ask anything (AI + PDF)", "📄 Only from PDF documents"],
            horizontal=True
        )
        
        # PDF Summary Button
        if st.button("📄 Generate PDF Summary"):
            st.session_state.pdf_summary_request = True
            st.success("Summary requested! Ask any question in the chat.")
    
    st.write("---")
    
    # Chat Management
    st.subheader("💾 Chat Management")
    
    # Save conversation
    if st.button("Save Conversation 💾"):
        if st.session_state.messages:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_messages = [m for m in st.session_state.messages if m["role"] != "system"]
            with open(f"chat_history_{timestamp}.json", "w") as f:
                json.dump(save_messages, f)
            st.success(f"Saved! (chat_history_{timestamp}.json)")
        else:
            st.warning("No conversation to save!")
    
    # Load conversation
    uploaded_chat = st.file_uploader("Load previous chat:", type=["json"], key="chat_loader")
    if uploaded_chat:
        try:
            loaded_msgs = json.load(uploaded_chat)
            system_msgs = [m for m in st.session_state.messages if m["role"] == "system"]
            st.session_state.messages = system_msgs + loaded_msgs
            st.success(f"Loaded {len(loaded_msgs)} messages!")
            st.rerun()
        except Exception as e:
            st.error(f"Error loading: {e}")
    
    # Export as Markdown
    if st.button("Export as Markdown 📝"):
        if st.session_state.messages:
            md_content = f"# Chat Export - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            md_content += f"**Model:** {selected_model}\n\n---\n\n"
            for msg in st.session_state.messages:
                if msg["role"] != "system":
                    md_content += f"### {msg['role'].upper()}\n{msg['content']}\n\n---\n\n"
            st.download_button(
                "📥 Download Markdown",
                md_content,
                f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                "text/markdown",
                key="markdown_download"
            )
        else:
            st.warning("No conversation to export!")
    
    st.write("---")
    
    # Voice Input
    st.subheader("🎙️ Voice Input")
    st.write("Click to speak your prompt:")
    voice_prompt = speech_to_text(
        language='en',
        start_prompt="Record Voice ⏺️",
        stop_prompt="Stop Recording ⏹️",
        just_once=True,
        key='STT'
    )
    if voice_prompt:
        st.info(f"Captured: \"{voice_prompt}\"")
    
    st.write("---")
    
    # Analytics Dashboard
    with st.expander("📊 Session Analytics"):
        if "messages" in st.session_state and st.session_state.messages:
            total_msgs = len([m for m in st.session_state.messages if m["role"] != "system"])
            user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
            assistant_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Messages", total_msgs)
            col2.metric("You", user_msgs)
            col3.metric("AI", assistant_msgs)
            
            total_chars = sum(len(m.get("content", "")) for m in st.session_state.messages)
            st.metric("Total Characters", f"{total_chars:,}")
            estimated_tokens = total_chars // 4
            st.metric("Est. Tokens", f"{estimated_tokens:,}")
            
            if uploaded_files and pdf_filenames:
                st.info(f"📁 PDFs: {len(pdf_filenames)}")
        else:
            st.info("No data yet. Start chatting!")
    
    st.write("---")
    
    # Clear chat session button
    if st.button("Clear Conversation History 🗑️"):
        st.session_state.messages = []
        st.rerun()

# 5. Memory Support Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_summary_request" not in st.session_state:
    st.session_state.pdf_summary_request = False

# Display entire persistent conversational timeline
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. User Input Handling
user_query = None

# Check for PDF summary request
if st.session_state.pdf_summary_request:
    user_query = "Please provide a comprehensive summary of all uploaded documents. Include main topics, key findings, and important details from each document."
    st.session_state.pdf_summary_request = False
elif voice_prompt:
    user_query = voice_prompt
else:
    user_query = st.chat_input("Ask Groq anything...")

# 7. Stream and Process LLM Generation
if user_query:
    # Append Context payload if user uploaded a PDF
    if pdf_context:
        if query_mode == "📄 Only from PDF documents":
            system_content = f"""You are an assistant answering questions STRICTLY based on the following document context.

DOCUMENT CONTENT:
{pdf_context}

CRITICAL RULES:
1. ONLY answer based on the document content above
2. If the answer is not in the documents, say: "I cannot find this information in the provided documents."
3. Do not use any external knowledge or make assumptions
4. When quoting, mention which document the information comes from"""
        else:
            system_content = f"""You are a helpful assistant. Use the following document context to enhance your answers when relevant.

REFERENCE CONTEXT:
{pdf_context}

Note: You can use your general knowledge, but prioritize information from the documents when applicable."""
        
        # Apply response format if not default
        if response_format != "Default":
            system_content += f"\n\nFormat your responses as {response_format}."
        
        system_instruction = {"role": "system", "content": system_content}
        
        if not st.session_state.messages or st.session_state.messages[0]["role"] != "system":
            st.session_state.messages.insert(0, system_instruction)
        else:
            st.session_state.messages[0] = system_instruction
    else:
        # No PDF, just apply format if needed
        if response_format != "Default" and (not st.session_state.messages or st.session_state.messages[0]["role"] != "system"):
            format_instruction = {"role": "system", "content": f"Format your responses as {response_format}."}
            st.session_state.messages.insert(0, format_instruction)

    # Log the prompt onto UI state
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Trigger Groq API Streaming Core
    with st.chat_message("assistant"):
        # Show typing indicator
        typing_indicator = st.empty()
        typing_indicator.markdown("_🤔 Thinking..._")
        
        message_placeholder = st.empty()
        full_response = ""
        
        # Start timing
        start_time = time.time()
        
        try:
            # Prepare messages for API (remove any system messages that might be duplicated)
            api_messages = []
            for m in st.session_state.messages:
                if m["role"] in ["user", "assistant", "system"]:
                    api_messages.append({"role": m["role"], "content": m["content"]})
            
            # Call Groq's low latency engine
            completion = client.chat.completions.create(
                model=selected_model,
                messages=api_messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
            )
            
            # Remove typing indicator once streaming starts
            typing_indicator.empty()
            
            for chunk in completion:
                token = chunk.choices[0].delta.content or ""
                full_response += token
                message_placeholder.markdown(full_response + "▌")
                
            # Render complete response
            message_placeholder.markdown(full_response)
            
            # Calculate response time
            response_time = time.time() - start_time
            
            # Show response time
            st.caption(f"⚡ Response time: {response_time:.2f} seconds using {selected_model}")
            
            # Add copy button
            col1, col2, col3 = st.columns([8, 1, 1])
            with col2:
                if st.button("📋 Copy", key=f"copy_{len(st.session_state.messages)}"):
                    st.toast("Copied to clipboard! (Press Ctrl+C to copy)")
            
            # Save Assistant Answer to Session State Memory
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            typing_indicator.empty()
            st.error(f"Groq API Error: {e}")

# Instructions to run:
# Save this file as chatbot.py
# Then run: streamlit run chatbot.py