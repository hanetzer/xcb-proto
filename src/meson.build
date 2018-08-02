
proto = [
  'bigreq.xml',
  'composite.xml',
  'damage.xml',
  'dpms.xml',
  'dri2.xml',
  'dri3.xml',
  'ge.xml',
  'glx.xml',
  'present.xml',
  'randr.xml',
  'record.xml',
  'render.xml',
  'res.xml',
  'screensaver.xml',
  'shape.xml',
  'shm.xml',
  'sync.xml',
  'xc_misc.xml',
  'xevie.xml',
  'xf86dri.xml',
  'xf86vidmode.xml',
  'xfixes.xml',
  'xinerama.xml',
  'xinput.xml',
  'xkb.xml',
  'xprint.xml',
  'xproto.xml',
  'xselinux.xml',
  'xtest.xml',
  'xvmc.xml',
  'xv.xml'
]

schema = 'xcb.xsd'

xmllint = find_program(['xmllint', '/usr/bin/xmllint'], required : false)
if xmllint.found()
  #do xml validation
  #foreach p : proto
  # run_command(xmllint, '--noout', '--schema', schema, p)
  #endforeach
  run_target('check-local',
      command : [ xmllint, '--noout', '--schema', schema, proto ]
  )
else
  warning('xmllint not found; unable to validate against schema.')
endif

if get_option('install-proto')
  install_data(
      files([ proto, schema ]),
      install_dir : join_paths(get_option('datadir'), 'xcb')
  )
endif
