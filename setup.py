#!/usr/bin/python

import sys
from distutils.core import setup, Extension
import string

VERSION = "0.6.2"
SHORT_DESC = "Network Boot and Update Server"
LONG_DESC = """
Cobbler is a network boot and update server.  Cobbler supports PXE, provisioning virtualized images, and reinstalling existing Linux machines.  The last two modes require a helper tool called 'koan' that integrates with cobbler.  Cobbler's advanced features include importing distributions from DVDs and rsync mirrors, kickstart templating, integrated yum mirroring, and built-in DHCP Management.  Cobbler has a Python API for integration with other GPL systems management applications.
"""

if __name__ == "__main__":
        # docspath="share/doc/koan-%s/" % VERSION
        manpath  = "share/man/man1/"
        cobpath  = "/var/lib/cobbler/"
        etcpath  = "/etc/cobbler/"
        wwwconf  = "/etc/httpd/conf.d/"
        wwwpath  = "/var/www/cobbler/"
        wwwgfx   = "/var/www/cobbler/webui/"
        initpath = "/etc/init.d/"
        logpath  = "/var/log/cobbler/"
        logpath2 = "/var/log/cobbler/kicklog"
        logpath3 = "/var/log/cobbler/syslog"
        snippets = "/var/lib/cobbler/snippets"
        wwwtmpl  = "/usr/share/cobbler/webui_templates/"
        vw_localmirror = "/var/www/cobbler/localmirror"
        vw_kickstarts  = "/var/www/cobbler/kickstarts"
        vw_kickstarts_sys  = "/var/www/cobbler/kickstarts_sys"
        vw_repomirror = "/var/www/cobbler/repo_mirror"
        vw_ksmirror   = "/var/www/cobbler/ks_mirror"
        vw_ksmirrorc  = "/var/www/cobbler/ks_mirror/config"
        vw_images     = "/var/www/cobbler/images"
        vw_distros    = "/var/www/cobbler/distros"
        vw_systems    = "/var/www/cobbler/systems"
        vw_profiles   = "/var/www/cobbler/profiles"
        vw_links      = "/var/www/cobbler/links"
        tftp_cfg      = "/tftpboot/pxelinux.cfg"
        tftp_images   = "/tftpboot/images"
        rotpath       = "/etc/logrotate.d"
        cgipath       = "/var/www/cgi-bin"
        setup(
                name="cobbler",
                version = VERSION,
                author = "Michael DeHaan",
                author_email = "mdehaan@redhat.com",
                url = "http://cobbler.et.redhat.com/",
                license = "GPL",
                packages = [
                    "cobbler",
                    "cobbler/yaml",
                    "cobbler/modules", 
                    "cobbler/webui",
                ],
                scripts = ["scripts/cobbler", "scripts/cobblerd"],
                data_files = [ 
                                
                                # cgi files
                                (cgipath,  ['scripts/findks.cgi', 'scripts/nopxe.cgi']),
                                (cgipath,  ['scripts/cobbler_webui.cgi']),
 
                                # miscellaneous config files
                                (rotpath,  ['config/cobblerd_rotate']),
                                (wwwconf,  ['config/cobbler.conf']),
                                (cobpath,  ['config/cobbler_hosts']),
                                (etcpath,  ['config/modules.conf']),
                                (etcpath,  ['config/auth.conf']),
                                (etcpath,  ['config/webui-cherrypy.cfg']),
                                (etcpath,  ['config/rsync.exclude']),
                                (initpath, ['config/cobblerd']),

                                # bootloaders and syslinux support files
                                (cobpath,  ['loaders/elilo-3.6-ia64.efi']),
                                (cobpath,  ['loaders/menu.c32']),

                                # sample kickstart files
                                (etcpath,  ['kickstarts/kickstart_fc5.ks']),
                                (etcpath,  ['kickstarts/kickstart_fc6.ks']),
                                (etcpath,  ['kickstarts/kickstart_fc6_domU.ks']),
                                (etcpath,  ['kickstarts/default.ks']),
 
                                # templates for DHCP and syslinux configs
				(etcpath,  ['templates/dhcp.template']),
				(etcpath,  ['templates/dnsmasq.template']),
				(etcpath,  ['templates/pxedefault.template']),
				(etcpath,  ['templates/pxesystem.template']),
				(etcpath,  ['templates/pxesystem_ia64.template']),
				(etcpath,  ['templates/pxeprofile.template']),

                                # useful kickstart snippets that we ship
                                (snippets, ['snippets/partition_select']),

                                # documentation
                                (manpath,  ['docs/cobbler.1.gz']),

                                # logfiles
                                (logpath,  []),
                                (logpath2, []),
                                (logpath3, []),

                                # web page directories that we own
                                (vw_localmirror,    []),
                                (vw_kickstarts,     []),
                                (vw_kickstarts_sys, []),
                                (vw_repomirror,     []),
                                (vw_ksmirror,       []),
                                (vw_ksmirrorc,      []),
                                (vw_distros,        []),
                                (vw_images,         []),
                                (vw_systems,        []),
                                (vw_profiles,       []),
                                (vw_links,          []),

                                # tftp directories that we own
                                (tftp_cfg,          []),
                                (tftp_images,       []),

                                # Web UI templates for object viewing & modification
                                # FIXME: other templates to add as they are created.
                                # slurp in whole directory?
                                (wwwtmpl,           ['webui_templates/distro_list.tmpl']),
                                (wwwtmpl,           ['webui_templates/profile_list.tmpl']),
                                (wwwtmpl,           ['webui_templates/profile_edit.tmpl']),
                                (wwwtmpl,           ['webui_templates/system_list.tmpl']),
                                (wwwtmpl,           ['webui_templates/system_edit.tmpl']),
                                #(wwwtmpl,           ['webui_templates/repo_list.tmpl']),

                                # Web UI common templates 
                                (wwwtmpl,           ['webui_templates/error_page.tmpl']),
                                (wwwtmpl,           ['webui_templates/master.tmpl']),
                                (wwwtmpl,           ['webui_templates/item.tmpl']),
                                (wwwtmpl,           ['webui_templates/index.tmpl']),

                                # Web UI kickstart file editing
                                (wwwtmpl,           ['webui_templates/ksfile_edit.tmpl']),
                                (wwwtmpl,           ['webui_templates/ksfile_list.tmpl']),
                                (wwwtmpl,           ['webui_templates/ksfile_view.tmpl']),

                                # Web UI support files
                                (wwwgfx,            []),
                                (wwwgfx,            ['webui_content/style.css']),
                                (wwwgfx,            ['webui_content/logo-cobbler.png']),
                                (wwwgfx,            ['webui_content/cobblerweb.css']),
 
                                # Directories to hold cobbler triggers
                                ("/var/lib/cobbler/triggers/add/distro/pre",      []),
                                ("/var/lib/cobbler/triggers/add/distro/post",     []),
                                ("/var/lib/cobbler/triggers/add/profile/pre",     []),
                                ("/var/lib/cobbler/triggers/add/profile/post",    []),
                                ("/var/lib/cobbler/triggers/add/system/pre",      []),
                                ("/var/lib/cobbler/triggers/add/system/post",     []),
                                ("/var/lib/cobbler/triggers/add/repo/pre",        []),
                                ("/var/lib/cobbler/triggers/add/repo/post",       []),
                                ("/var/lib/cobbler/triggers/delete/distro/pre",   []),
                                ("/var/lib/cobbler/triggers/delete/distro/post",  []),
                                ("/var/lib/cobbler/triggers/delete/profile/pre",  []),
                                ("/var/lib/cobbler/triggers/delete/profile/post", []),
                                ("/var/lib/cobbler/triggers/delete/system/pre",   []),
                                ("/var/lib/cobbler/triggers/delete/system/post",  []),
                                ("/var/lib/cobbler/triggers/delete/repo/pre",     []),
                                ("/var/lib/cobbler/triggers/delete/repo/post",    [])
                             ],
                description = SHORT_DESC,
                long_description = LONG_DESC
        )

