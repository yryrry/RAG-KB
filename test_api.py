# 导入SDK：openai库就是HTTP客户端，帮我们封装网络请求，不用手写requests
from openai import OpenAI
# python‑dotenv，读取本地.env文件里的密钥
from dotenv import load_dotenv
import os

# 加载.env文件，把里面的键值对读到程序的环境变量
load_dotenv()

# -------- 构建DeepSeek客户端对象 --------
ds_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),   # 从环境变量取出密钥
    base_url="https://api.deepseek.com"      # API服务地址，请求发到这个网址
)

# -------- 构建硅基流动客户端对象 --------
sf_client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url="https://api.siliconflow.cn/v1"
)

# 1️⃣调用大模型对话接口
print("===== 1.测试DeepSeek对话接口 =====")
resp_chat = ds_client.chat.completions.create(
    model="deepseek-chat",    # 指定要调用哪个模型
    messages=[{"role":"user","content":"简单介绍RAG是什么，一句话"}], # 对话消息列表
    temperature=0.3           # 随机性参数
)
# 从返回结果取出模型回答文本
print("回答：", resp_chat.choices[0].message.content)
# 取出token统计
print("token消耗：", resp_chat.usage)


# 2️⃣调用Embedding向量接口（硅基流动bge‑m3）
print("\n===== 2.测试硅基流动 bge‑m3 embedding =====")
emb_resp = sf_client.embeddings.create(
    model="BAAI/bge-m3",
    input=["人工智能应用开发"]   # 需要转向量的文本，可以传多个字符串
)
emb_vector = emb_resp.data[0].embedding
print(f"向量维度：{len(emb_vector)}")
print(f"向量前10个数字：{emb_vector[:10]}")
