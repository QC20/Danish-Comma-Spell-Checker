import re

# 1. Komma mellem ledsætninger:
def tilføj_komma_mellem_ledsætninger(text):
    corrected_text = re.sub(r'([^.!?"])([.!?"])?\s+([A-ZÆØÅ])', r'\1\2 \3', text)
    return corrected_text

# 2. Komma ved indskudte ledsætninger:
def tilføj_komma_i_indskudte_ledsætninger(text):
    corrected_text = re.sub(r', (som|der) [^,]+, ', r', \1, ', text)
    return corrected_text
    
# 3. Komma i opremsninger:
def tilføj_komma_i_opremsninger(text):
    corrected_text = re.sub(r'(\w+)\s+og\s+(\w+)(?:\s+og\s+(\w+))?$', r'\1, \2, \3', text)
    return corrected_text
    
# 4. Komma omkring ikke-restrictive bisætninger:
def tilføj_komma_omkring_bisætninger(text):
    corrected_text = re.sub(r'([a-zæøå]), ([a-zæøå])', r'\1, \2', text)
    return corrected_text
    
# 5. Komma ved direkte henvendelse:
def tilføj_komma_i_direkte_henvendelser(text):
    corrected_text = re.sub(r'([A-ZÆØÅ][a-zæøå]+),', r'\1,', text)
    return corrected_text
    
# 6. Komma før "fordi" i ledsætninger:
def tilføj_komma_før_fordi(text):
    corrected_text = re.sub(r'([a-zæøå]), fordi', r'\1, fordi', text)
    return corrected_text
    
# 7. Komma i citater:
def tilføj_komma_i_citater(text):
    corrected_text = re.sub(r'"(.*?)"', r'"\1,"', text)   
    return corrected_text

# 8. Komma efter "og" i forbindelse med udeladelser:
def tilføj_komma_efter_og_ved_udeladelser(text):
    corrected_text = re.sub(r'(\w+)\s+og\s+(\w+)\s+\.\.\.\s+(\w+)$', r'\1, \2 ... \3', text)
    return corrected_text
    
# 9. Komma ved indirekte spørgsmål:
def tilføj_komma_i_indirekte_spørgsmål(text):
    corrected_text = re.sub(r'(hvad|hvem|hvor|hvorfor|hvilken|hvilket|hvilke|hvilke)\s+[^,]+,\s+(\w+)', r'\1, \2', text)
    return corrected_text
    
# 10. Komma før ledsætningen "så":
def tilføj_komma_før_så(text):
    corrected_text = re.sub(r'(\w+)\s+så', r'\1, så', text)
    return corrected_text
    
# 11. Tilføj komma efter ledsætninger, der starter med "hvor"
def tilføj_komma_efter_hvor(text):
    corrected_text = re.sub(r'(hvor .+?), (.+)', r'\1, \2', text)
    return corrected_text
    
# 12. Tilføj komma efter adverbet i en sammenligning
def tilføj_komma_i_stedordssammenligninger(text):
    corrected_text = re.sub(r'(\w+ er [\w\s]+), ([\w\s]+ end .+)', r'\1, \2', text)
    return corrected_text
    
comma_correction_functions = [
    tilføj_komma_mellem_ledsætninger,
    tilføj_komma_i_indskudte_ledsætninger,
    tilføj_komma_i_opremsninger,
    tilføj_komma_omkring_bisætninger,
    tilføj_komma_i_direkte_henvendelser,
    tilføj_komma_før_fordi,
    tilføj_komma_i_citater,
    tilføj_komma_efter_og_ved_udeladelser,
    tilføj_komma_i_indirekte_spørgsmål,
    tilføj_komma_før_så,
    tilføj_komma_efter_hvor,
    tilføj_komma_i_stedordssammenligninger,]

# Example text with potential comma errors
text = "Dansk eksempel tekst."

# Apply each correction function to the text
for correction_function in comma_correction_functions:
    text = correction_function(text)
# Print the corrected text
print(text)
