{
  'targets': [
    {
      'target_name': 'mdb_v8',
      'product_prefix': '',
      'type': 'loadable_module',
      'cflags': [ '-fPIC', '-Wno-missing-field-initializers', '-Wno-sign-compare',
                  '-Os', '-fno-asynchronous-unwind-tables', '-ffunction-sections', ],
      'ldflags': [ '-Wl,--gc-sections', '-Wl,--strip-all', ],
      'sources': [
        'mdb_v8.c',
        'mdb_v8_cfg.c',
        'v8cfg.h',
        'v8dbg.h',
      ],
      'link_settings': {
        'libraries': [
          '-lproc',
          '-lavl',
        ],
      },
    },
  ],
}
