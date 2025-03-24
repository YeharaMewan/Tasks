import google.generativeai as genai
import os
from dotenv import load_dotenv
import time
import colorama
from colorama import Fore, Style

# Initialize colorama for colored terminal output
colorama.init()

# Load environment variables (API key)
load_dotenv()

# Configure the API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Enhanced product information database
products = {
    "smartphone": {
        "name": "ProTech X1",
        "price": 799.99,
        "features": [
            "6.7-inch AMOLED display with 120Hz refresh rate",
            "5G connectivity with support for all major carriers",
            "Triple camera system (108MP main, 12MP ultrawide, 10MP telephoto)",
            "4500mAh battery with all-day battery life and 65W fast charging",
            "8GB RAM and 256GB storage",
            "Snapdragon 8 Gen 2 processor",
            "IP68 water and dust resistance",
            "Gorilla Glass Victus front and back"
        ],
        "colors": ["Midnight Black", "Ocean Blue", "Silver Moon"],
        "warranty": "1-year limited warranty with optional extended coverage",
        "unique_selling_points": [
            "Industry-leading camera quality in low light",
            "Fastest charging in its class",
            "Premium build materials"
        ],
        "target_audience": "Photography enthusiasts, tech-savvy professionals, premium segment users",
        "comparable_products": ["iPhone 15 Pro", "Samsung Galaxy S24", "Google Pixel 8"],
        "customer_reviews": {
            "average_rating": 4.7,
            "highlights": [
                "Users love the camera quality",
                "Battery life exceeds expectations",
                "Premium design and build quality"
            ]
        }
    },
    "laptop": {
        "name": "UltraBook Pro",
        "price": 1299.99,
        "features": [
            "14-inch 4K OLED display with 400 nits brightness",
            "16GB LPDDR5 RAM (expandable to 32GB)",
            "1TB NVMe SSD with read speeds up to 7000MB/s",
            "Intel Core i7-13700H processor (14 cores, 20 threads)",
            "Intel Iris Xe Graphics",
            "12-hour battery life with fast charging (80% in 1 hour)",
            "Thunderbolt 4, USB-C, HDMI, and SD card reader",
            "Backlit keyboard with 1.5mm key travel"
        ],
        "colors": ["Graphite", "Silver", "Rose Gold"],
        "warranty": "2-year manufacturer warranty with accidental damage protection",
        "unique_selling_points": [
            "Ultra-slim design at just 0.6 inches thick",
            "Best-in-class keyboard for comfortable typing",
            "Studio-quality microphones and speakers"
        ],
        "target_audience": "Professionals, content creators, business users",
        "comparable_products": ["MacBook Pro 14", "Dell XPS 13", "Lenovo ThinkPad X1"],
        "customer_reviews": {
            "average_rating": 4.8,
            "highlights": [
                "Exceptional build quality and performance",
                "Display is stunning for creative work",
                "Battery life consistently meets or exceeds expectations"
            ]
        }
    },
    "headphones": {
        "name": "SoundWave Max",
        "price": 249.99,
        "features": [
            "Active noise cancellation with transparency mode",
            "40-hour battery life (30 hours with ANC enabled)",
            "Hi-Fi sound with custom 40mm drivers",
            "Bluetooth 5.2 with multipoint connection",
            "Comfortable memory foam ear cushions",
            "Touch controls and voice assistant support",
            "App support with EQ customization",
            "Quick charge (5 hours of playback from 10-minute charge)"
        ],
        "colors": ["Black", "White", "Navy Blue"],
        "warranty": "18-month warranty covering manufacturing defects",
        "unique_selling_points": [
            "Industry-leading noise cancellation",
            "Superior comfort for all-day wear",
            "Audiophile-grade sound quality"
        ],
        "target_audience": "Music enthusiasts, frequent travelers, remote workers",
        "comparable_products": ["Sony WH-1000XM5", "Bose QuietComfort", "Apple AirPods Max"],
        "customer_reviews": {
            "average_rating": 4.6,
            "highlights": [
                "Noise cancellation rivals much more expensive brands",
                "Battery life is exceptional",
                "Great balance of bass and clarity"
            ]
        }
    },
    "tablet": {
        "name": "SlateTab Ultra",
        "price": 549.99,
        "features": [
            "10.9-inch Liquid Retina display with TrueTone",
            "A14 Bionic chip with 6-core CPU and 4-core GPU",
            "128GB/256GB/512GB storage options",
            "12MP wide camera and 7MP front camera",
            "All-day battery life (up to 10 hours)",
            "USB-C connector with 20W fast charging",
            "Support for Smart Keyboard and Pencil",
            "Stereo speakers in landscape mode"
        ],
        "colors": ["Space Gray", "Silver", "Rose Gold", "Sky Blue"],
        "warranty": "1-year limited warranty with AppleCare+ option",
        "unique_selling_points": [
            "Perfect balance of performance and portability",
            "Ecosystem integration with other TechWorld products",
            "Optimized for both productivity and entertainment"
        ],
        "target_audience": "Students, creative professionals, casual users",
        "comparable_products": ["iPad Air", "Samsung Galaxy Tab S8", "Microsoft Surface Go"],
        "customer_reviews": {
            "average_rating": 4.7,
            "highlights": [
                "Display quality is outstanding",
                "Performance handles everything from gaming to productivity",
                "Perfect size for reading and media consumption"
            ]
        }
    }
}

# Create a custom instruction for the sales agent
sales_agent_instructions = """
You are an AI-powered sales representative for a tech company called TechWorld. Your role is to assist customers, 
answer product-related questions, make personalized recommendations, and facilitate the sales process.

Remember these key guidelines:
1. Be friendly, helpful, and knowledgeable about the products in our catalog
2. Ask clarifying questions if you need more information to make recommendations
3. Never make up product specifications - only use the product data provided
4. If a customer wants a product we don't offer, suggest the closest alternative
5. For complex inquiries beyond your knowledge, offer to connect them with a human representative
6. When comparing products, highlight our product's strengths while being honest about limitations
7. Ensure privacy by not asking for personal information beyond what's needed for product recommendations
8. Use a conversational, natural tone that builds rapport with the customer

When recommending products, explain why they match the customer's needs and reference specific features that 
address their requirements. Share relevant customer reviews when appropriate.
"""

# Few-shot examples to improve model responses
few_shot_examples = [
    {
        "role": "user",
        "parts": ["I'm looking for a smartphone with a good camera."]
    },
    {
        "role": "model",
        "parts": ["I'd be happy to help you find a smartphone with an excellent camera! Our ProTech X1 features a triple camera system with a 108MP main sensor, a 12MP ultrawide, and a 10MP telephoto lens with 3x optical zoom. It's perfect for photography enthusiasts. The camera also has advanced night mode capabilities. Would you like to know more about this phone or are there other specific camera features you're looking for?"]
    },
    {
        "role": "user",
        "parts": ["What colors does it come in?"]
    },
    {
        "role": "model",
        "parts": ["The ProTech X1 comes in three beautiful colors: Midnight Black, Ocean Blue, and Silver Moon. The Midnight Black has a matte finish, the Ocean Blue has a unique shimmering effect that changes slightly depending on the lighting, and the Silver Moon has a classic metallic look. All three colors have a premium glass back. Do you have a preference among these options?"]
    }
]

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro", 
                              system_instruction=sales_agent_instructions)

# Create a chat session with few-shot examples
chat = model.start_chat(history=few_shot_examples)

def format_product_context(product_type, details):
    """Format product details in a comprehensive way"""
    context = f"Product information for {details['name']} ({product_type}):\n"
    context += f"- Price: ${details['price']}\n"
    context += f"- Features: {', '.join(details['features'])}\n"
    context += f"- Available in: {', '.join(details['colors'])}\n"
    context += f"- Warranty: {details['warranty']}\n"
    context += f"- Key selling points: {', '.join(details['unique_selling_points'])}\n"
    context += f"- Target audience: {details['target_audience']}\n"
    context += f"- Customer reviews: {details['customer_reviews']['average_rating']}/5 stars\n"
    context += f"- Review highlights: {', '.join(details['customer_reviews']['highlights'])}\n"
    return context

def sales_agent(user_input):
    """Process user input and return the sales agent's response"""
    
    # Add product context to the prompt when relevant keywords are detected
    product_context = ""
    for product_type, details in products.items():
        if product_type in user_input.lower():
            product_context = format_product_context(product_type, details)
    
    # Check for comparison queries
    if "compare" in user_input.lower() or "vs" in user_input.lower() or "versus" in user_input.lower():
        detected_products = []
        for product_type in products:
            if product_type in user_input.lower():
                detected_products.append(product_type)
        
        if len(detected_products) >= 2:
            product_context = "Comparison information:\n"
            for product_type in detected_products:
                product_context += format_product_context(product_type, products[product_type]) + "\n"
    
    # Send the prompt with product context
    try:
        if product_context:
            response = chat.send_message(f"[PRODUCT CONTEXT:\n{product_context}]\n\nCustomer: {user_input}")
        else:
            response = chat.send_message(f"Customer: {user_input}")
        
        return response.text
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Let me connect you with a human representative who can assist you further."

def display_welcome():
    """Display a welcome message with ASCII art"""
    welcome_text = """
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║             Welcome to TechWorld Virtual Assistant         ║
    ║                                                            ║
    ║  Your AI-powered shopping companion for tech products!     ║
    ║                                                            ║
    ║  Ask about our:                                            ║
    ║    • Smartphones (ProTech X1)                              ║
    ║    • Laptops (UltraBook Pro)                               ║
    ║    • Headphones (SoundWave Max)                            ║
    ║    • Tablets (SlateTab Ultra)                              ║
    ║                                                            ║
    ║  Type 'exit' or 'quit' to end the conversation             ║
    ║  Type 'help' for assistance                                ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """
    print(Fore.CYAN + welcome_text + Style.RESET_ALL)

def simulate_typing(text):
    """Simulate typing effect for more natural conversation"""
    print(Fore.GREEN + "TechWorld Assistant: " + Style.RESET_ALL, end="")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.005)  # Adjust typing speed as needed
    print()

def show_help():
    """Display help information"""
    help_text = """
    Here are some things you can ask me about:
    
    • Product information: "Tell me about your smartphones"
    • Specific features: "Does the UltraBook Pro have good battery life?"
    • Comparisons: "How does the ProTech X1 compare to iPhone 15?"
    • Recommendations: "I need headphones for travel"
    • Pricing: "What's the price of the SlateTab Ultra?"
    • Availability: "What colors do your laptops come in?"
    
    I'm here to help you find the perfect tech product for your needs!
    """
    print(Fore.YELLOW + help_text + Style.RESET_ALL)

def run_conversation():
    """Run an interactive conversation with the sales agent"""
    display_welcome()
    
    simulate_typing("Hello! Welcome to TechWorld. I'm your virtual shopping assistant. How can I help you today?")
    
    while True:
        user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL)
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            simulate_typing("Thank you for chatting with us today. Have a great day!")
            break
        
        if user_input.lower() == 'help':
            show_help()
            continue
        
        print(Fore.YELLOW + "Thinking..." + Style.RESET_ALL)
        agent_response = sales_agent(user_input)
        simulate_typing(agent_response)

if __name__ == "__main__":
    run_conversation()