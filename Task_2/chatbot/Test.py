"""
Test script for the TechWorld Sales Agent
Run this file to test different customer interaction scenarios
"""

import os
import time
import colorama
from colorama import Fore, Style
from dotenv import load_dotenv

# Import the sales_agent function from your main file
# Change the import to match your actual file name
try:
    from Agent import sales_agent, products
except ImportError:
    print(Fore.RED + "Error: Cannot import from Agent.py. Make sure the file exists and is in the same directory." + Style.RESET_ALL)
    exit(1)

# Initialize colorama for colored terminal output
colorama.init()

def test_scenario(scenario_name, conversation):
    """Run a test scenario with predefined conversation turns"""
    print(Fore.CYAN + "\n" + "="*70 + Style.RESET_ALL)
    print(Fore.CYAN + f"TEST SCENARIO: {scenario_name}" + Style.RESET_ALL)
    print(Fore.CYAN + "="*70 + "\n" + Style.RESET_ALL)
    
    for turn in conversation:
        print(Fore.BLUE + f"Customer: {turn}" + Style.RESET_ALL)
        
        try:
            print(Fore.YELLOW + "Processing..." + Style.RESET_ALL)
            start_time = time.time()
            response = sales_agent(turn)
            end_time = time.time()
            
            print(Fore.GREEN + f"Sales Agent: {response}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"[Response time: {end_time - start_time:.2f} seconds]" + Style.RESET_ALL)
            print()
            
        except Exception as e:
            print(Fore.RED + f"ERROR: {str(e)}" + Style.RESET_ALL)
            print()
            continue
    
    print(Fore.CYAN + "="*70 + Style.RESET_ALL)
    print(Fore.CYAN + f"END OF SCENARIO: {scenario_name}" + Style.RESET_ALL)
    print(Fore.CYAN + "="*70 + "\n" + Style.RESET_ALL)

def verify_environment():
    """Verify that environment variables are properly set up"""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print(Fore.RED + "ERROR: Gemini API key not found in .env file!" + Style.RESET_ALL)
        print(Fore.YELLOW + "Please create a .env file with your API key in this format:" + Style.RESET_ALL)
        print(Fore.WHITE + "GEMINI_API_KEY=your_api_key_here" + Style.RESET_ALL)
        return False
    
    print(Fore.GREEN + "✓ API key found in .env file" + Style.RESET_ALL)
    return True

def verify_product_data():
    """Verify that product data is properly loaded"""
    if not products:
        print(Fore.RED + "ERROR: Product database is empty!" + Style.RESET_ALL)
        return False
    
    for product_type, details in products.items():
        required_fields = ['name', 'price', 'features', 'colors']
        missing_fields = [field for field in required_fields if field not in details]
        
        if missing_fields:
            print(Fore.RED + f"ERROR: Product '{product_type}' is missing required fields: {missing_fields}" + Style.RESET_ALL)
            return False
    
    print(Fore.GREEN + f"✓ Product database loaded with {len(products)} products" + Style.RESET_ALL)
    return True

def run_all_tests():
    """Run all test scenarios"""
    if not verify_environment() or not verify_product_data():
        print(Fore.RED + "Test setup failed. Please fix the issues above." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "Starting test scenarios...\n" + Style.RESET_ALL)

    # Scenario 1: Product inquiry and recommendation
    scenario1 = [
        "I need a new smartphone with good camera quality.",
        "What's the battery life like on the ProTech X1?",
        "Do you have it in Ocean Blue?",
        "Great, I'd like to purchase one."
    ]
    test_scenario("Product Inquiry and Purchase Flow", scenario1)
    
    # Scenario 2: Comparison between products
    scenario2 = [
        "I'm looking for a laptop for video editing and programming.",
        "How does the UltraBook Pro compare to a MacBook Pro?",
        "What about the warranty options?",
        "That sounds good, but I'm still not sure which is better for me."
    ]
    test_scenario("Product Comparison", scenario2)
    
    # Scenario 3: Customer with budget constraints
    scenario3 = [
        "I want wireless headphones but I'm on a tight budget.",
        "That's a bit expensive for me. Do you have anything under $150?",
        "What's the sound quality like on your budget options?",
        "I'll think about it and come back later."
    ]
    test_scenario("Budget Constraints", scenario3)
    
    # Scenario 4: Technical support inquiry
    scenario4 = [
        "My laptop battery doesn't last as long as advertised.",
        "I've only had it for 3 months.",
        "It's the UltraBook Pro model.",
        "What's your return and repair policy?"
    ]
    test_scenario("Customer Support", scenario4)
    
    # Scenario 5: Product availability inquiry
    scenario5 = [
        "Do you have tablets available?",
        "Tell me more about the SlateTab Ultra.",
        "Is it good for reading and watching videos?",
        "Do you offer any accessories for it?"
    ]
    test_scenario("Product Availability", scenario5)

    print(Fore.GREEN + "All test scenarios completed!" + Style.RESET_ALL)

if __name__ == "__main__":
    run_all_tests()