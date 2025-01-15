#include "ld2420_sensor.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace ld2420 {

static const char *const TAG = "LD2420.sensor";

void LD2420Sensor::dump_config() {
  ESP_LOGCONFIG(TAG, "LD2420 Sensor:");
  LOG_SENSOR("  ", "Distance", this->distance_sensor_);
  LOG_SENSOR("  ", "Gate Energy 1", this->energy_sensors_[0]);
  LOG_SENSOR("  ", "Gate Energy 2", this->energy_sensors_[1]);
  LOG_SENSOR("  ", "Gate Energy 3", this->energy_sensors_[2]);
  LOG_SENSOR("  ", "Gate Energy 4", this->energy_sensors_[3]);
  LOG_SENSOR("  ", "Gate Energy 5", this->energy_sensors_[4]);
  LOG_SENSOR("  ", "Gate Energy 6", this->energy_sensors_[5]);
  LOG_SENSOR("  ", "Gate Energy 7", this->energy_sensors_[6]);
  LOG_SENSOR("  ", "Gate Energy 8", this->energy_sensors_[7]);
  LOG_SENSOR("  ", "Gate Energy 9", this->energy_sensors_[8]);
  LOG_SENSOR("  ", "Gate Energy 10", this->energy_sensors_[9]);
  LOG_SENSOR("  ", "Gate Energy 11", this->energy_sensors_[10]);
  LOG_SENSOR("  ", "Gate Energy 12", this->energy_sensors_[11]);
  LOG_SENSOR("  ", "Gate Energy 13", this->energy_sensors_[12]);
  LOG_SENSOR("  ", "Gate Energy 14", this->energy_sensors_[13]);
  LOG_SENSOR("  ", "Gate Energy 15", this->energy_sensors_[14]);
  LOG_SENSOR("  ", "Gate Energy 16", this->energy_sensors_[15]);
}

}  // namespace ld2420
}  // namespace esphome
