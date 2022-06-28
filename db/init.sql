CREATE DATABASE Task;
use Task;

CREATE TABLE predict (
event_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  features JSON,
  predictions JSON
);

INSERT INTO predict (features, predictions) VALUES ('["1","2"]', '["3", "4"]');
