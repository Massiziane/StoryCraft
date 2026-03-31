from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text: str = Field(description="the text of the option presented to the user")
    nextNode: Dict[str, Any] = Field(description="the next node content and its options")


class StoryModels(BaseModel):
    content: str = Field(description="The main content of the stroy node")
    isEnding: bool = Field(description="Whether this node is an ending node")
    isWinningEnding: bool = Field(description="Whether this node is a winning ending node")
    options: Optional[List[StoryOptionLLM]] = Field(description="The options for this node")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode = StoryNodeLLM = Field(description="The root node of the story")

    
