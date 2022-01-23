# -*- coding: utf-8 -*-
from typing import Any
from typing import Optional
from typing import Text
from typing import Tuple

_re_number = ...  # type: Any

def to_normal(pinyin: Text, v_to_u: bool = ...) -> Text: ...

def to_tone(pinyin: Text) -> Text: ...

def to_tone2(pinyin: Text, v_to_u: bool = ..., neutral_tone_with_5: bool = ...) -> Text: ...

def to_tone3(pinyin: Text, v_to_u: bool = ..., neutral_tone_with_5: bool = ...) -> Text: ...

def to_initials(pinyin: Text, strict: bool = ...) -> Text: ...

def to_finals(pinyin: Text, strict: bool = ..., v_to_u: bool = ...) -> Text: ...

def tone_to_normal(tone: Text, v_to_u: bool = ...) -> Text: ...

def tone_to_tone2(tone: Text, v_to_u: bool = ..., neutral_tone_with_5: bool = ...) -> Text: ...

def tone_to_tone3(tone: Text, v_to_u: bool = ..., neutral_tone_with_5: bool = ...) -> Text: ...

def tone2_to_normal(tone2: Text, v_to_u: bool = ...) -> Text: ...

def tone2_to_tone(tone2: Text,) -> Text: ...

def tone2_to_tone3(tone2: Text, v_to_u: bool = ...) -> Text: ...

def tone3_to_normal(tone3: Text, v_to_u: bool = ...) -> Text: ...

def tone3_to_tone(tone3: Text) -> Text: ...

def tone3_to_tone2(tone3: Text, v_to_u: bool = ...) -> Text: ...

def _improve_tone3(tone3: Text, neutral_tone_with_5: bool = ...) -> Text: ...

def _get_number_from_pinyin(pinyin: Text) -> Optional[int]: ...

def _v_to_u(pinyin: Text, replace: bool = ...) -> Text: ...

def _fix_v_u(origin_py: Text, new_py: Text, v_to_u: bool) -> Text: ...
