from langchain_core.documents import Document
# LangChain 为文本单元及相关元数据实现了一个 Document 抽象。它包含三个属性
# page_content：代表内容的字符串。
# metadata：包含任意元数据的字典。
# id：（可选）文档的字符串标识符。
# metadata 可以记录文档的来源、它与其他文档的关系以及其他信息。单个 Document 通常代表一个更大文档的分块（chunk）。
documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
]