from enum  import Enum

class userPurposeType(Enum):
    pass  # TODO: implement
purpose_map={
"其他":userPurposeType.text,
"文本生成":userPurposeType.text,
"音频生成":userPurposeType.Audio,
"视频生成":userPurposeType.Video,
"图片描述":userPurposeType.ImageDescribe,
"图片生成":userPurposeType.ImageGeneration,
"基于知识库":userPurposeType.RAG,
"问候语":userPurposeType.Hello,
"PPT生成":userPurposeType.PPT,
"Word生成":userPurposeType.Docx,
"网络搜索":userPurposeType.InternetSearch,
"基于知识图谱":userPurposeType.KnowledgeGraph,
"深度研究":userPurposeType.DeepResearch,
}

