###################################################################################################
### Project Configuration #########################################################################
###################################################################################################

extensions = [
    # core extensions
    'sphinx.ext.inheritance_diagram',
    # Markdown support
    'myst_parser', 
    # API documentation support
    'autoapi',
]

root_doc = 'index'
exclude_patterns = ['_build']
html_theme = "pydata_sphinx_theme"

suppress_warnings = [
    "myst.header", # suppress warnings of the kind "WARNING: Non-consecutive header level increase; H1 to H3"
]

####################################################################################################
### Theme html Configuration #######################################################################
####################################################################################################


####################################################################################################
### Extension Configuration ########################################################################
####################################################################################################

# autoapi Configuration ################################################
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html#customisation-options

autoapi_dirs = [
    '../test_library',
]

autoapi_options = [
    'members',
    'undoc-members',
    'private-members',
    'show-inheritance',
    'show-module-summary',
    'show-inheritance-diagram'
]

graphviz_output_format = 'svg' # https://pydata-sphinx-theme.readthedocs.io/en/stable/examples/graphviz.html#inheritance-diagram

autoapi_python_class_content = 'both'
autoapi_member_order = 'groupwise'
autoapi_root = 'api'
autoapi_keep_files = False