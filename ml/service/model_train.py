import asyncio

from ml.db.db import get_db
from ml.service.aggregation import Aggregation
from ml.service.prediction import BrokeClassifier, BrokeRegressor


async def main():
    db = get_db()
    await db.connect()
    agg = Aggregation()
    await agg.aggregate_data()
    await db.disconnect()

    train_df = agg.get_data()
    classification_target = train_df["target_class"]
    regression_target = train_df["target_reg"].astype(float)

    train_df.drop(
        ["target_class", "target_reg", "car_id"],
        axis=1,
        inplace=True,
    )
    train_df[["car_rating"]] = train_df[["car_rating"]].astype(float)
    train_df[["year_to_start"]] = train_df[["year_to_start"]].astype(float)
    train_df[["riders"]] = train_df[["riders"]].astype(float)
    train_df[["year_to_work"]] = train_df[["year_to_work"]].astype(float)

    train_df[["avg_rating"]] = train_df[["avg_rating"]].astype(float)
    train_df[["avg_ride_duration"]] = train_df[["avg_ride_duration"]].astype(float)
    train_df[["min_ride_duration"]] = train_df[["min_ride_duration"]].astype(float)
    train_df[["max_ride_duration"]] = train_df[["max_ride_duration"]].astype(float)
    train_df[["avg_ride_cost"]] = train_df[["avg_ride_cost"]].astype(float)
    train_df[["avg_speed"]] = train_df[["avg_speed"]].astype(float)
    train_df[["avg_speed_max"]] = train_df[["avg_speed_max"]].astype(float)
    train_df[["sum_stop_times"]] = train_df[["sum_stop_times"]].astype(float)
    train_df[["total_distance"]] = train_df[["total_distance"]].astype(float)
    train_df[["total_refueling"]] = train_df[["total_refueling"]].astype(float)
    train_df[["avg_user_rating"]] = train_df[["avg_user_rating"]].astype(float)
    train_df[["accidents"]] = train_df[["accidents"]].astype(float)

    classification_model = BrokeClassifier(train_df, classification_target)
    classification_model.train()
    classification_model.save_model()

    regression_model = BrokeRegressor(train_df, regression_target)
    regression_model.train()
    regression_model.save_model()


if __name__ == "__main__":
    asyncio.run(main())
