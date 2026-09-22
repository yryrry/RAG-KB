# 1. choices
API返回结果里的`choices`是**模型生成答案的数组列表**。
大模型可以一次性生成多条回答，放在这个数组中，日常使用默认只返回1条。

示例简化返回结构：
```json
"choices": [
    {
        "message": {
            "role": "assistant",
            "content": "这里是大模型回答文本"
        },
        "finish_reason": "stop"
    }
]
```
- `choices[0]`：取第一条（默认唯一）回答
- `message.content`：**真正的回答文字**
- `finish_reason`：结束原因
  - `stop`：正常回答结束
  - `length`：达到token上限，被截断

> 面试简答：choices是模型输出结果数组，存放模型生成的回答，一般取索引0拿到返回文本。

# 2. token消耗（prompt_tokens / completion_tokens / total_tokens）
- **prompt_tokens**：提示词token，**你发给大模型的输入文本**消耗的token。包含system、user的所有内容。
- **completion_tokens**：补全token，**大模型新生成输出的回答**消耗的token。输出token一般更贵。
- **total_tokens** = prompt_tokens + completion_tokens，本次请求总共消耗token，服务商按token计费。

> 面试简答：prompt_tokens是输入提示词消耗token；completion_tokens是模型生成回答消耗token；total_tokens是两者总和，作为计费依据。

# 3. temperature
控制**大模型输出的随机度、创造性**，取值范围一般`0 ~ 2`。
- `temperature=0`：输出**最确定、最保守**，每次相同提问答案几乎一样，适合知识库问答、RAG场景，减少幻觉。
- 0~0.5：稳定，适合RAG、数据提取
- 0.7左右：有一定创造性，适合文案、聊天
- 接近2：随机性极强，想象力高，但容易编造内容、产生幻觉

> 面试简答：temperature控制模型输出随机性。值越低结果越确定、重复性高；值越高创造性越强，但更容易出现幻觉。RAG知识库问答一般设置0~0.3。

