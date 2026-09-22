from openai import OpenAI
from dotenv import load_dotenv
import os
import numpy as np

# 加载环境变量
load_dotenv()
client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url="https://api.siliconflow.cn/v1"
)

# 调用硅基bge-m3，获取文本向量
def get_embedding(text: str):
    resp = client.embeddings.create(
        model="BAAI/bge-m3",
        input=text,
        timeout=60
    )
    return resp.data[0].embedding

# 计算余弦相似度
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)


# 测试文本
text_a = "RAG是检索增强生成技术"
text_b = "检索增强生成可以降低大模型幻觉"
text_c = "猫咪喜欢吃鱼"

# 获取向量
vec_a = get_embedding(text_a)
vec_b = get_embedding(text_b)
vec_c = get_embedding(text_c)

# 输出相似度
print("文本A：", text_a)
print("文本B：", text_b)
print("文本C：", text_c)
print("\nA 和 B 的余弦相似度：", cosine_similarity(vec_a, vec_b))
print("A 和 C 的余弦相似度：", cosine_similarity(vec_a, vec_c))
