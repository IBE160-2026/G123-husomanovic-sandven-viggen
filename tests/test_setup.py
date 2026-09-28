import importlib

import pytest


@pytest.mark.parametrize(
    "module",
    ["streamlit", "chromadb", "fastembed", "anthropic", "pypdf", "yaml", "dotenv"],
)
def test_dependency_importable(module):
    importlib.import_module(module)


def test_src_package_importable():
    importlib.import_module("src")
