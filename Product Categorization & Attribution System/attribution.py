import pandas as pd
from preprocess import preprocess
from client_rules import client_rule_tag
from model import train_model

CONFIDENCE_THRESHOLD = 0.7

def run_attribution(df, client="Client_A"):
    df = preprocess(df)

    # Client-specific rule tagging
    df["rule_category"] = df["clean_text"].apply(
        lambda x: client_rule_tag(x, client)
    )

    rule_df = df[df["rule_category"].notnull()].copy()
    ml_df = df[df["rule_category"].isnull()].copy()

    if not ml_df.empty and not rule_df.empty:
        model, vectorizer = train_model(
            rule_df["clean_text"],
            rule_df["rule_category"]
        )

        X = vectorizer.transform(ml_df["clean_text"])
        probs = model.predict_proba(X)
        preds = model.classes_[probs.argmax(axis=1)]
        confidence = probs.max(axis=1)

        ml_df["final_category"] = [
            p if c >= CONFIDENCE_THRESHOLD else "MANUAL_REVIEW_REQUIRED"
            for p, c in zip(preds, confidence)
        ]
    else:
        ml_df["final_category"] = "MANUAL_REVIEW_REQUIRED"

    rule_df["final_category"] = rule_df["rule_category"]

    final_df = pd.concat([rule_df, ml_df]).sort_index()
    final_df["client"] = client

    return final_df
