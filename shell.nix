let
  pkgs = import <nixpkgs> {};
  testDependencies = [
    pkgs.python3Packages.setuptools
    pkgs.mkdocs
  ];
  mkdcomments = pkgs.python3Packages.buildPythonPackage {
    pname = "python-markdown-comments";
    version = "master";
    src = ./.;

    buildInputs = [
      pkgs.python3Packages.markdown
    ];
    checkInputs = testDependencies;
  };
in
  pkgs.mkShell {
    buildInputs = [
      mkdcomments
    ] ++ testDependencies;
  }
