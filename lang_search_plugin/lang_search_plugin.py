from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.structure.nav import Navigation
from mkdocs.config import config_options
import logging

log = logging.getLogger("mkdocs.plugins." + __name__)

class LangSearchPlugin(BasePlugin):
    config_scheme = (
        ('default_language', config_options.Type(str, default='en')),
    )

    def __init__(self):
        super().__init__()
        log.info("LangSearchPlugin initialized")

    def on_pre_page(self, page: Page, config, files):
        """Process each page before it is converted to HTML."""
        try:
            log.info(f"Processing page: {page.file.src_path}")
            language = page.file.src_path.split('/')[0]
            page.meta['language'] = language
            log.debug(f"Set language for {page.file.src_path} to {language}")
        except Exception as e:
            log.error(f"Error processing page {page.file.src_path}: {e}")
        return page

    def on_nav(self, nav: Navigation, config, files):
        """Modify navigation items based on default language."""
        try:
            log.info("Modifying navigation items based on default language")
            default_language = self.config['default_language']
            nav.items = [item for item in nav.items if item.file.src_path.startswith(default_language)]
            log.debug(f"Filtered navigation items to default language: {default_language}")
        except Exception as e:
            log.error(f"Error modifying navigation items: {e}")
        return nav

    def on_page_context(self, context, page: Page, config, nav: Navigation):
        """Set the search index context for each page."""
        try:
            log.info(f"Setting search index context for page: {page.file.src_path}")
            default_language = self.config['default_language']
            context['search'] = {
                'index': [p for p in nav.pages if p.file.src_path.startswith(default_language)]
            }
            log.debug(f"Search context set for default language: {default_language}")
        except Exception as e:
            log.error(f"Error setting search index context for page {page.file.src_path}: {e}")
        return context

    def on_config(self, config):
        """Handle updates to the configuration."""
        try:
            log.info("Configuring LangSearchPlugin")
            # Additional configuration steps can be added here
        except Exception as e:
            log.error(f"Error configuring LangSearchPlugin: {e}")
        return config
