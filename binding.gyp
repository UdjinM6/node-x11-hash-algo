{
    "targets": [
        {
            "target_name": "x11",
            "sources": [
                "x11hash.cc",
                "x11.c",
                "sha3/sph_blake.c",
                "sha3/sph_bmw.c",
                "sha3/sph_cubehash.c",
                "sha3/sph_echo.c",
                "sha3/sph_groestl.c",
                "sha3/sph_jh.c",
                "sha3/sph_keccak.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_skein.c"
            ],
            "include_dirs": [
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
