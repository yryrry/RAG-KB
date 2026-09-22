# 模块1 大模型基础 高频问答
## Q1：什么是token？API返回中的prompt_tokens、completion_tokens、total_tokens分别是什么含义？
A：token是大模型处理文本的最小子词单元，可以是单词、汉字、文字片段。中文大约1个汉字对应1~2个token，MaaS平台按照token计费。
- prompt_tokens：输入提示词消耗的token，包含system、user的全部内容；
- completion_tokens：模型新生成回答所消耗的token，输出token一般价格更高；
- total_tokens = prompt_tokens + completion_tokens，代表本次请求总共消耗的token。
>面试简答：token是文本的最小处理单元；prompt_tokens是输入消耗token，completion_tokens是模型输出消耗token，total_tokens为总和，作为计费依据。

## Q2：什么是上下文窗口，有什么限制？RAG开发里要注意什么？
A：上下文窗口是大模型单次请求能够一次性接收处理的最大token总量。system提示词、用户问题、对话历史、检索返回的文档片段、模型输出全部占用这个窗口额度。
当总token超过上限，会直接报错，或者自动截断最前面的文本。
RAG开发中需要控制检索返回chunk的总长度，防止超出上下文窗口限制。
>面试简答：上下文窗口是大模型单次可处理的最大token上限，所有输入输出都占用窗口额度；RAG需要控制检索片段长度，避免超限。

## Q3：temperature参数的含义，取值影响，RAG场景推荐设置？
A：temperature控制大模型输出的随机度与创造性，取值范围一般0~2。
- temperature=0：输出最确定、保守，相同提问答案几乎一致，适合知识库问答，减少幻觉；
- 0~0.5：结果稳定，适合RAG、数据提取；
- 0.7左右：有一定创造性，适合聊天、文案生成；
- 接近2：随机性极强，想象力高，但容易编造内容，幻觉概率高。
>面试简答：temperature控制模型输出随机性。值越低结果越确定、重复性高；值越高创造性越强，但更容易出现幻觉。RAG知识库问答一般设置0~0.3。

## Q4：什么是大模型幻觉？有哪些缓解方案？
A：幻觉指大模型自信地输出错误、编造、不存在的信息，文字看起来通顺合理，但内容虚假。
缓解手段：
1. 使用RAG引入真实外部知识库，让模型基于参考文档作答；
2. 调低temperature，降低随机编造概率；
3. 在prompt增加约束，要求不知道就直接说明，禁止编造；
4. 要求回答时引用原文片段。
>面试简答：幻觉是大模型编造虚假信息；可以使用RAG、降低temperature、增加prompt约束等方式缓解。

## Q5：OpenAI兼容接口 messages消息结构，system / user / assistant 分别是什么作用？
A：messages是消息数组，用来存放对话历史，按顺序传给模型。
- system：系统提示，设定模型角色、回答规则，优先级最高；
- user：用户的提问内容；
- assistant：模型上一轮返回的回答。
>面试简答：messages是对话数组；system设定角色和回答规则，user是用户提问，assistant保存模型历史回答，DeepSeek、硅基流动这类MaaS都兼容这套结构。
