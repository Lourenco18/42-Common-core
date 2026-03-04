import alchemy.grimoire as grimoire

print("=== Circular Curse Breaking ===\n")

print("Testing validation:")
print(grimoire.validate_ingredients("fire air"))
print(grimoire.validate_ingredients("dragon scales"))

print("\nTesting spell recording:")
print(grimoire.record_spell("Fireball", "fire air"))
print(grimoire.record_spell("Dark Magic", "shadow"))

print("\nCircular dependency avoided using late imports!")
