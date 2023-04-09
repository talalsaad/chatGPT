import os
import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": '''cheak if there is splling mistake in (File: 55 - Copy (2).png
Device Name: Talal
Processor: Ilth Gen Intel(R) Core(TM) i5-113567 @ 24OGHz
Installed RAM: 16.0 GB (15.7 GB usable)
Device ID: DOEECSFE-CDSD-4ACE-84C4-574AACCIE52O
System Type: 64-bit operating system; x64-based processor
//////////////////////////////////////////////////////////////////////

File: 55 - Copy (3).png
Device Name: Talal
Processor: Ilth Gen Intel(R) Core(TM) i5-113567 @ 24OGHz
Installed RAM: 16.0 GB (15.7 GB usable)
Device ID: DOEECSFE-CDSD-4ACE-84C4-574AACCIE52O
System Type: 64-bit operating system; x64-based processor
//////////////////////////////////////////////////////////////////////

File: 55 - Copy.png
Device Name: Talal
Processor: Ilth Gen Intel(R) Core(TM) i5-113567 @ 24OGHz
Installed RAM: 16.0 GB (15.7 GB usable)
Device ID: DOEECSFE-CDSD-4ACE-84C4-574AACCIE52O
System Type: 64-bit operating system; x64-based processor
//////////////////////////////////////////////////////////////////////

File: 55.png
Device Name: Talal
Processor: Ilth Gen Intel(R) Core(TM) i5-113567 @ 24OGHz
Installed RAM: 16.0 GB (15.7 GB usable)
Device ID: DOEECSFE-CDSD-4ACE-84C4-574AACCIE52O
System Type: 64-bit operating system; x64-based processor
//////////////////////////////////////////////////////////////////////
) and give me only the crrected data '''}
  ]
)
print(completion.choices[0])
