"""
Constants
"""

# Django
from django.utils.text import slugify

# AA Survey
from aa_survey import __version__

github_url: str = "https://github.com/ppfeufer/aa-survey"
verbose_name: str = "AA-Surves - Manage surveys in Alliance Auth"
verbose_name_slug: str = slugify(verbose_name, allow_unicode=True)
user_agent: str = f"{verbose_name_slug} v{__version__} {github_url}"

# All internal URLs need to start with this prefix
# to prevent conflicts with user generated forum URLs
INTERNAL_URL_PREFIX = "-"
