from transformers import AutoProcessor
from transformers import AutoModelForCausalLM


checkpoint = "microsoft/git-base"
processor = AutoProcessor.from_pretrained(checkpoint)

checkpoint = "hieudinhpro/git-base-on-diffuision-dataset2"
model = AutoModelForCausalLM.from_pretrained(checkpoint)