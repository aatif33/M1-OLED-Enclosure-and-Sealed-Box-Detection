# Dataset split report

| Split | Target ratio | Actual image count | Actual ratio |
|---|---:|---:|---:|
| Train | 70% | TODO | TODO |
| Validation | 20% | TODO | TODO |
| Test | 10% | TODO | TODO |

## Leakage prevention
Describe how images from the same video, capture session, physical item, or burst were kept in one split. A random image-level split is not sufficient when adjacent frames are near-duplicates.

## Verification
- [ ] No filename overlap
- [ ] No duplicate file hashes across splits
- [ ] Related capture sessions grouped before splitting
- [ ] Matching labels copied and checked
