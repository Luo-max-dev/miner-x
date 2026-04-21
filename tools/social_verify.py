from holehe import core as holehe_core
import asyncio

async def verify_social_presence(email):
    """
    Check if an email is registered on major social platforms using Holehe OSINT.
    Supports 120+ platforms (LinkedIn, Twitter, Instagram, etc.)
    """
    if not email: return False
    
    out = []
    # Import submodules from holehe
    modules = holehe_core.import_submodules("holehe.modules")
    
    # We focus on core B2B channels for better speed
    target_modules = ['linkedin', 'twitter', 'instagram', 'facebook']
    
    for module in modules:
        try:
            m_name = module.__name__.split('.')[-1]
            if m_name in target_modules:
                await module.check(email, out)
        except Exception:
            continue
            
    # Return True if any social profile is found
    return any(d['exists'] for d in out)

if __name__ == "__main__":
    # Test
    asyncio.run(verify_social_presence("test@example.com"))
