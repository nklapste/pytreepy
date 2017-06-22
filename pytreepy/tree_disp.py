""" module that creates a terminal printable display of a directory tree """
import os

SET_SPACE = 30


def list_files(startpath, note_dict):
    indentval = str(SET_SPACE - len('directory:') - 1)
    format_str = ' %-s %-'+indentval+'s %-s'
    print(format_str % ('directory:', '', 'info:' ))
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        try:
            addon_info = note_dict[os.path.join(root)]
        except KeyError:
            addon_info = ""
        finally:
            # formate the addon_info evenly for directorys
            indentval = str(SET_SPACE - len(indent))
            format_str = '%-s %-'+indentval+'s %-30s'
            print(format_str % (indent, os.path.basename(root)+':/', addon_info))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            try:
                addon_info = note_dict[os.path.join(root, f)]
            except KeyError:
                addon_info = ""
            finally:
                # format the addon_info evenly
                indentval = str(SET_SPACE - len(indent) - 4)
                format_str = '%-s %-'+indentval+'s %-30s'
                print(format_str % (subindent, f, addon_info))

test = dict()
test['/home/ndklaps/Desktop/pytreepy/README.md'] = 'bleh asd'
test['/home/ndklaps/Desktop/pytreepy'] = 'bleh asd'
test['/home/ndklaps/Desktop/pytreepy/test/tes.tx'] = 'bleh asd'
test['/home/ndklaps/Desktop/pytreepy/pytreepy'] = 'bleh asd'
test['/home/ndklaps/Desktop/pytreepy/pytreepy/tree_disp.py'] = 'bleh asd'
list_files('/home/ndklaps/Desktop/pytreepy', test)
