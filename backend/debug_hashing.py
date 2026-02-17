from core.security import get_password_hash, verify_password

def debug_hashing():
    password = "securepassword123"
    print(f"Testing password: '{password}' (Length: {len(password)})")
    
    try:
        hashed = get_password_hash(password)
        print(f"✅ Hashing successful: {hashed[:10]}...")
        
        is_valid = verify_password(password, hashed)
        print(f"✅ Verification successful: {is_valid}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_hashing()
