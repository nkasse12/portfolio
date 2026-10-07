# CODE_RUNNER: Homework - Crack the Final Transmission using slicing, methods, and formatting

raw_transmission = "  2026-09-15,GHOST,THE-EAGLE-LANDS-AT-DAWN,87  "

# TODO 1: Use .strip() to remove the outer whitespace, then .split(",") to break it into fields.
#         Print segments. Since this is a real CSV row (no leading/trailing marker), there
#         should be exactly 4 fields and no stray empty strings.
segments = raw_transmission.strip().split(",")
print("Segments:", segments)

# TODO 2: Use indexing on segments to pull out the date, agent, message code, and confidence.
date = segments[0]
agent = segments[1]
message_code = segments[2]
confidence_str = segments[3]
print("Date:", date, "| Agent:", agent, "| Message code:", message_code, "| Confidence:", confidence_str)

# TODO 3: Use SLICING (not a method) on date to confirm it starts with the year "2026".
year_check = date[:4]
print("Year check:", year_check)

# TODO 4: Use .replace() to turn the dashes in message_code into spaces. Save it as message.
message = message_code
message_code = message_code.replace("-", " ")
print("Message:", message_code)

# TODO 5: Use .lower() and the `in` operator to check whether "dawn" appears anywhere in message.
found_dawn = "dawn" in message_code.lower()
print("Found 'dawn':", found_dawn)

# TODO 6: Use an f-string with "|" separators to build a Markdown table row of the decoded fields,
#         in the form:
#         "| <date> | <agent> | <message> | <confidence_str>% |"
markdown_row = f"| {date} | {agent} | {message_code} | {confidence_str}% |"
print("Markdown row:", markdown_row)

# TODO 7: Use an f-string to build a JSON-style line for the same fields, mixing "{", "}", ":", and ","
#         the way real systems pass structured data. Use str(found_dawn).lower() for the boolean, since
#         JSON uses lowercase true/false instead of Python's True/False. Form:
#         {"date": "<date>", "agent": "<agent>", "message": "<message>", "confidence": <confidence_str>, "contains_dawn": <found_dawn lowercase>}
json_line = f'{{"date": "{date}", "agent": "{agent}", "message": "{message_code}", "confidence": {confidence_str}, "contains_dawn": {str(found_dawn).lower()}}}'
print("JSON line:", json_line)