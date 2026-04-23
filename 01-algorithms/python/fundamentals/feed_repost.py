# Feed Repost Detector
#
# You're building a social feed. Users sometimes accidentally double-post
# the same content within a short window. Given a chronological list of
# post IDs and a window size `k`, return True if any post ID appears twice
# within `k` positions of each other. Otherwise return False.
#
# "Within k positions" means the two indexes differ by AT MOST k.
# (i.e. abs(i - j) <= k, i != j, and posts[i] == posts[j])
#
# Examples:
#   posts = [1, 2, 3, 1], k = 3        -> True   (post 1 at idx 0 and 3, diff = 3)
#   posts = [1, 0, 1, 1], k = 1        -> True   (post 1 at idx 2 and 3, diff = 1)
#   posts = [1, 2, 3, 1, 2, 3], k = 2  -> False  (closest repeat is diff = 3)
#   posts = [9, 9], k = 1              -> True
#   posts = [5, 5], k = 0              -> False  (same index doesn't count)
#
# Constraints:
#   - posts is a list of ints (post IDs, not necessarily sorted)
#   - k is a non-negative int
#   - return a bool
#
# Target: O(n) time, O(n) space.


def has_recent_repost(posts: list[int], k: int) -> bool:
    seen_posts = {}
    for i, post in enumerate(posts):
        if post not in seen_posts:
            seen_posts[post] = i
        else:
            delta = i - seen_posts[post]
            if delta <= k:
                return True
            seen_posts[post] = i
    return False


def has_recent_repost_v2(posts: list[int], k: int) -> bool:
    seen_posts = {}
    for i, post in enumerate(posts):
        if post in seen_posts and i - seen_posts[post] <= k:
            return True
        seen_posts[post] = i
    return False


# v1 tests
print(has_recent_repost([1, 2, 3, 1], 3))        # True
print(has_recent_repost([1, 0, 1, 1], 1))        # True
print(has_recent_repost([1, 2, 3, 1, 2, 3], 2))  # False
print(has_recent_repost([9, 9], 1))              # True
print(has_recent_repost([5, 5], 0))              # False

# v2 tests
print(has_recent_repost_v2([1, 2, 3, 1], 3))        # True
print(has_recent_repost_v2([1, 0, 1, 1], 1))        # True
print(has_recent_repost_v2([1, 2, 3, 1, 2, 3], 2))  # False
print(has_recent_repost_v2([9, 9], 1))              # True
print(has_recent_repost_v2([5, 5], 0))              # False
