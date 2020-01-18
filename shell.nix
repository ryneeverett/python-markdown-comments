let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  pname = "python-markdown-comments";
  buildInputs = [
    pkgs.pythonPackages.markdown
  ];
}
