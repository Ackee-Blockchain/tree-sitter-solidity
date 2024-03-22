from pathlib import Path
from platform import system
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CustomBuildExt(build_ext):
    def run(self):
        super().run()

        for output_file in self.get_outputs():
            path = Path(output_file)
            if path.suffix == ".pyd":
                path.rename(path.with_name("solidity.dll"))
            elif path.suffix == ".so":
                path.rename(path.with_name("solidity.so"))


with Path(__file__).parent.joinpath("README.md").open() as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="abch_tree_sitter_solidity",
    version="1.2.2",
    author="Ackee Blockchain",
    url="https://github.com/Ackee-Blockchain/tree-sitter-solidity",
    license="MIT",
    platforms=["any"],
    python_requires=">=3.7",
    install_requires=["abch-tree-sitter>=1.0.1"],
    setup_requires=["abch-tree-sitter>=1.0.1"],
    description="Solidity grammar for the Tree-sitter parsing library",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["tree_sitter_solidity"],
    package_data={"tree_sitter_solidity": ["solidity.so", "solidity.dll"]},
    project_urls={"Source": "https://github.com/Ackee-Blockchain/tree-sitter-solidity"},
    data_files=[("src", ["src/parser.c", "src/tree_sitter/parser.h"])],
    ext_modules=[
        Extension(
            name="tree_sitter_solidity.solidity",
            sources=["src/parser.c", "src/entry_point.c"],
            include_dirs=["src"],
            extra_compile_args=(
                ["-fPIC", "-std=c99"] if system() != "Windows" else None
            ),
        )
    ],
    cmdclass={"build_ext": CustomBuildExt},
)
