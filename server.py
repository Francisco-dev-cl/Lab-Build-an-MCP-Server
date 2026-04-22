from fastmcp import FastMCP
from pathlib import Path
import json

# Initializing our MCP server instance
mcp = FastMCP("Connoisseur-Server")

# Data paths
DATA_DIR = Path(__file__).parent
CULINARY_MAP_PATH = DATA_DIR / "California-Culinary-Map.txt"
RESTAURANT_DATA_PATH = DATA_DIR / "structured-restaurant-data.json"
REVIEW_DATA_PATH = DATA_DIR / "augmented-user-review.json"

# Helper functions
def load_restaurant_data() -> list[dict]:
    with open(RESTAURANT_DATA_PATH, "r") as f:
        return json.load(f)

def load_review_data() -> list[dict]:
    with open(REVIEW_DATA_PATH, "r") as f:
        return json.load(f)

# --- MCP RESOURCE ---
@mcp.resource("culinary-map://california")
def get_culinary_map() -> str:
    """The full raw California Culinary Map text."""
    return CULINARY_MAP_PATH.read_text()

# --- TOOL 1: Get Restaurant Info ---
@mcp.tool()
def get_restaurant_info(restaurant_name: str) -> str:
    """Search for a restaurant by name and return its structured details."""
    restaurants = load_restaurant_data()
    query = restaurant_name.lower().strip()
    matches = [r for r in restaurants if query in r["name"].lower() or r["name"].lower() in query]
    
    if not matches:
        return json.dumps({
            "status": "not_found",
            "message": f"No restaurant found matching '{restaurant_name}'.",
            "suggestion": "Try a partial name like 'Iron' or 'Sakura'."
        }, indent=2)
    
    return json.dumps({"status": "found", "count": len(matches), "results": matches}, indent=2)

# --- TOOL 2: Recommend by Vibe ---
@mcp.tool()
def recommend_by_vibe(vibe: str) -> str:
    """Find restaurants that match a given vibe or atmosphere keyword."""
    restaurants = load_restaurant_data()
    vibe_lower = vibe.lower().strip()
    
    structured_matches = []
    for r in restaurants:
        vibes_list = [v.lower() for v in r.get("vibes", [])]
        if vibe_lower in vibes_list or vibe_lower in r.get("description", "").lower():
            structured_matches.append({
                "name": r["name"], "neighborhood": r["neighborhood"], 
                "cuisine": r["cuisine"], "rating": r["rating"], "vibes": r["vibes"]
            })
    
    raw_text = CULINARY_MAP_PATH.read_text()
    paragraphs = raw_text.split("\n\n")
    text_excerpts = [p.strip()[:300] for p in paragraphs if vibe_lower in p.lower() and p.strip()]
    
    return json.dumps({
        "vibe_searched": vibe,
        "structured_matches": structured_matches,
        "raw_text_excerpts": text_excerpts[:5]
    }, indent=2)

# --- TOOL 3: Get Review ---
@mcp.tool()
def get_review(restaurant_name: str) -> str:
    """Retrieve the full review for a restaurant."""
    reviews = load_review_data()
    query = restaurant_name.lower().strip()
    matching_review = next((r for r in reviews if query in r["restaurant_name"].lower()), None)
    
    if not matching_review:
        return json.dumps({
            "status": "not_found",
            "message": f"No review found for '{restaurant_name}'."
        }, indent=2)
    
    return json.dumps({
        "status": "found",
        "restaurant": matching_review["restaurant_name"],
        "reviewer": matching_review["reviewer"],
        "rating": matching_review["rating"],
        "review_text": matching_review["review_text"]
    }, indent=2)

if __name__ == "__main__":
    mcp.run()
