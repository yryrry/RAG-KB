from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#创建客户端实例
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"  ,
)

prompt = "一句话解释RAG是什么"

temp_list = [0,0.3,0.7,1,2]

for temp in temp_list:
    print(f"\n====temperature = {temp}====")
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system","content":"你是ai开发助手,回答简洁"},
            {"role":"user","content":prompt},
        ],
        temperature=temp,
        timeout=60,
    )
    # 从返回结果choices数组取出第一条回答的文本
    content = resp.choices[0].message.content
    # usage 是token消耗统计对象
    usage = resp.usage
    # finish_reason：模型停止生成的原因
    finish_reason = resp.choices[0].finish_reason

    # 打印输出结果
    print("回答内容：", content)
    print(f"prompt_tokens: {usage.prompt_tokens}")  # 输入token
    print(f"completion_tokens: {usage.completion_tokens}")  # 生成输出token
    print(f"total_tokens: {usage.total_tokens}")  # 总token
    print(f"finish_reason: {finish_reason}")