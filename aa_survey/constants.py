"""
Constants
"""

from django.utils.text import slugify

from aa_survey import __version__

github_url = "https://github.com/ppfeufer/aa-survey"
verbose_name = "AA-Surves - Manage surveys in Alliance Auth"
verbose_name_slug = slugify(verbose_name, allow_unicode=True)
user_agent = f"{verbose_name_slug} v{__version__} {github_url}"

# All internal URLs need to start with this prefix
# to prevent conflicts with user generated forum URLs
INTERNAL_URL_PREFIX = "-"
