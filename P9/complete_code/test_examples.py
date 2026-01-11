"""
Test data for cards_logic.py doctests.
This file provides pre-defined variables 
for easy reference when testing the functions.
"""
# =============================================================================
# TEST DATA FOR add_card()
# =============================================================================

# Basic addition test
card_list = ['diamonds', 'hearts']
# add 'spades'
expected = ['diamonds', 'hearts', 'spades']

# =============================================================================
# TEST DATA FOR remove_card()
# =============================================================================

# Basic removal test
card_list = ['diamonds', 'hearts']
# remove 'hearts'
expected = ['diamonds']

# Error case - card not in list

# =============================================================================
# TEST DATA FOR count_card_occurrences()
# =============================================================================

# Multiple occurrences test
card_list = ['diamonds', 'hearts', 'spades', 'diamonds']
# count = 'diamonds'
expected = 2

# Zero occurrences test


# =============================================================================
# TEST DATA FOR swap_card_positions()
# =============================================================================

# Basic swap test
card_list = ['spades', 'hearts', 'clubs', 'diamonds']
# swap 0 and 3
expected = ['diamonds', 'hearts', 'clubs', 'spades']

# Error case - index out of bounds


# =============================================================================
# TEST DATA FOR reposition_card()
# =============================================================================

# Basic reposition test
card_list = ['hearts', 'spades', 'clubs']
# reposition 'spades' to index 0
expected = ['spades', 'hearts', 'clubs']

# Error case - index out of bounds
# Error case - card doesn't exist

# =============================================================================
# TEST DATA FOR cut_card_list_in_two()
# =============================================================================

# Basic cut test
card_list = ['hearts', 'hearts', 'spades', 'spades', 'spades']
expected = ['spades', 'spades', 'spades', 'hearts', 'hearts']

# Empty list test
# Single card test
