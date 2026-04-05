from typing import Optional

from pydantic import BaseModel, Field

from enums.tone import Tone
from enums.verbosity import Verbosity


class PromptToPptxRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Prompt used to generate the presentation")
    filename: Optional[str] = Field(
        default=None,
        description="Optional output filename without path",
    )
    template: str = Field(
        default="general",
        description="Template to use for the presentation",
    )
    tone: Tone = Field(
        default=Tone.PROFESSIONAL,
        description="The tone to use for the presentation",
    )
    verbosity: Verbosity = Field(
        default=Verbosity.STANDARD,
        description="How verbose the presentation should be",
    )
    instructions: Optional[str] = Field(
        default=None,
        description="Additional generation instructions",
    )
    web_search: bool = Field(
        default=False,
        description="Whether to enable web search during generation",
    )
