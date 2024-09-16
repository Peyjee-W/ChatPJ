from flask import Flask, render_template, request, jsonify
import openai
import threading
import webbrowser
import time
import os

app = Flask(__name__)

# 设置 API 密钥
openai.api_key = "your-api-key"  # 设置你的 OpenAI API 密钥

# 设置正确的 API 基础 URL
openai.api_base = "https://free.gpt.ge/v1"

# 保存所有会话历史
conversations = {}
current_conversation_id = 1  # 当前对话 ID

# 初始化一个新的对话会话
def new_conversation():
    global current_conversation_id
    conversation_id = current_conversation_id
    current_conversation_id += 1
    conversations[conversation_id] = [
        {"role": "system", "content": "你是一个聪明的对话助手。"}  # 系统消息
    ]
    return conversation_id

# 创建第一个对话
current_conversation = new_conversation()

@app.route("/")
def index():
    return render_template("index.html", conversations=conversations.keys())  # 渲染静态网页并传递所有对话

@app.route("/chat", methods=["POST"])
def chat():
    global current_conversation
    user_message = request.json.get("message")

    # 将用户输入添加到当前对话历史
    conversations[current_conversation].append({"role": "user", "content": user_message})

    # 调用 OpenAI API 生成回复
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=conversations[current_conversation],
        )
        # 获取模型的回复
        assistant_reply = completion.choices[0].message.content
        # 将模型回复添加到当前对话历史
        conversations[current_conversation].append({"role": "assistant", "content": assistant_reply})
        return jsonify({"reply": assistant_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["POST"])
def reset():
    global current_conversation
    # 重新创建一个新的对话
    current_conversation = new_conversation()
    return jsonify({"success": True, "conversation_id": current_conversation})

@app.route("/switch", methods=["POST"])
def switch_conversation():
    global current_conversation
    # 获取要切换到的会话 ID
    conversation_id = int(request.json.get("conversation_id"))
    if conversation_id in conversations:
        current_conversation = conversation_id
        return jsonify({"success": True, "conversation_id": current_conversation})
    else:
        return jsonify({"success": False, "error": "会话不存在"})

@app.route("/get_conversation/<int:conversation_id>")
def get_conversation(conversation_id):
    if conversation_id in conversations:
        return jsonify(conversations[conversation_id])
    else:
        return jsonify({"error": "会话不存在"}), 404

def open_browser():
    # 只在主进程中打开浏览器，避免在调试器自动重启时重复打开
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        time.sleep(1)  # 等待1秒，确保服务器启动后再打开浏览器
        webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # 在新线程中打开浏览器
    threading.Thread(target=open_browser).start()
    # 启动 Flask 服务器
    app.run(debug=True)
