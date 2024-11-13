import numpy as np
import pytest

from cognee.tasks.chunks import chunk_by_paragraph
from cognee.tests.unit.processing.chunks.test_input import INPUT_TEXTS


@pytest.mark.parametrize(
    "input_text,paragraph_length,batch_paragraphs",
    [
        (INPUT_TEXTS["english_text"], 64, True),
        (INPUT_TEXTS["english_text"], 64, False),
        (INPUT_TEXTS["english_text"], 256, True),
        (INPUT_TEXTS["english_text"], 256, False),
        (INPUT_TEXTS["english_text"], 1024, True),
        (INPUT_TEXTS["english_text"], 1024, False),
        (INPUT_TEXTS["english_lists"], 64, True),
        (INPUT_TEXTS["english_lists"], 64, False),
        (INPUT_TEXTS["english_lists"], 256, True),
        (INPUT_TEXTS["english_lists"], 256, False),
        (INPUT_TEXTS["english_lists"], 1024, True),
        (INPUT_TEXTS["english_lists"], 1024, False),
        (INPUT_TEXTS["python_code"], 64, True),
        (INPUT_TEXTS["python_code"], 64, False),
        (INPUT_TEXTS["python_code"], 256, True),
        (INPUT_TEXTS["python_code"], 256, False),
        (INPUT_TEXTS["python_code"], 1024, True),
        (INPUT_TEXTS["python_code"], 1024, False),
        (INPUT_TEXTS["chinese_text"], 64, True),
        (INPUT_TEXTS["chinese_text"], 64, False),
        (INPUT_TEXTS["chinese_text"], 256, True),
        (INPUT_TEXTS["chinese_text"], 256, False),
        (INPUT_TEXTS["chinese_text"], 1024, True),
        (INPUT_TEXTS["chinese_text"], 1024, False),
    ],
)
def test_chunk_by_paragraph_isomorphism(input_text, paragraph_length, batch_paragraphs):
    chunks = chunk_by_paragraph(input_text, paragraph_length, batch_paragraphs)
    reconstructed_text = "".join([chunk["text"] for chunk in chunks])
    assert (
        reconstructed_text == input_text
    ), f"texts are not identical: {len(input_text) = }, {len(reconstructed_text) = }"
