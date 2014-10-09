from util import github

from nose.tools import *

def test_make_github_url_github_pages():
    remote = 'danvk/danvk.github.io.git'
    eq_('https://github.com/danvk/danvk.github.io',
        github.make_github_url(remote))
