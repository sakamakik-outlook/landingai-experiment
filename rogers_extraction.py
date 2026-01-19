import json
import asyncio
from pathlib import Path
from landingai_ade import AsyncLandingAIADE

async def main():
    # Initialize the async client
    client = AsyncLandingAIADE()

    # First, parse the document to get markdown
    parse_response = await client.parse(
        # document=Path("interest_note_pages_1_11.pdf"),
        document=Path("rogers_13_14_15.pdf"),
        model="dpt-2-latest"
    )

    # Load schema from JSON file
    with open("rogers_schema.json", "r") as f:
        schema_json = f.read()

    # Extract structured data using the schema
    extract_response = await client.extract(
        schema=schema_json,
        markdown=parse_response.markdown,
        model="extract-latest"
    )

    # Save extraction data to JSON file
    with open("rogers_out_data.json", "w") as f:
        json.dump(extract_response.extraction, f, indent=2)

    # Save extraction metadata to JSON file
    with open("rogers_out_metadata.json", "w") as f:
        json.dump(extract_response.extraction_metadata, f, indent=2)

    print("Saved extraction to rogers_out_data.json")
    print("Saved metadata to rogers_out_metadata.json")

if __name__ == "__main__":
    asyncio.run(main())