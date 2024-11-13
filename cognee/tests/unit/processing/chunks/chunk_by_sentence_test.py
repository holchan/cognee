import pytest
import numpy as np
from cognee.tasks.chunks import chunk_by_sentence
from cognee.tests.unit.processing.chunks.test_input import INPUT_TEXTS

@pytest.mark.parametrize("input_text", [
    INPUT_TEXTS["english_text"],
    INPUT_TEXTS["english_lists"],
    INPUT_TEXTS["python_code"],
    INPUT_TEXTS["chinese_text"]
])

def test_chunk_by_sentence_isomorphism(input_text):
    chunks = chunk_by_sentence(input_text)
    reconstructed_text = "".join([chunk[2] for chunk in chunks])
    assert reconstructed_text == input_text, f"texts are not identical: {len(input_text) = }, {len(reconstructed_text) = }"

