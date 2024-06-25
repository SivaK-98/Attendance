{pkgs}: {
  deps = [
    pkgs.glibcLocales
    pkgs.mongosh
    pkgs.rustc
    pkgs.pkg-config
    pkgs.openssl
    pkgs.libxcrypt
    pkgs.libiconv
    pkgs.cargo
  ];
}
