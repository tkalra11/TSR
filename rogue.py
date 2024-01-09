from rouge_score import rouge_scorer
import globalvar

scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
scores = scorer.score('The quick brown fox jumps over the lazy dog' , 'The quick brown dog jumps on the active log.')

print(scores)