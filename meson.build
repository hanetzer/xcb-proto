project('xcb-proto', version: '1.13', license: 'MIT')

subdir('src')

pkg = import('pkgconfig')

pkg.generate(
    name: 'xcb-proto',
    description: 'X protocol descriptions for XCB',
    variables: [
      'datarootdir=${prefix}/share',
      'xcbincludedir=${datadir}/xcb'
    ]
)
