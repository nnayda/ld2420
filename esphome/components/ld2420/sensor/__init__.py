import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, DEVICE_CLASS_DISTANCE, UNIT_CENTIMETER,UNIT_WATT,DEVICE_CLASS_ENERGY
from .. import ld2420_ns, LD2420Component, CONF_LD2420_ID

LD2420Sensor = ld2420_ns.class_("LD2420Sensor", sensor.Sensor, cg.Component)

CONF_MOVING_DISTANCE = "moving_distance"
CONF_GATE_ENERGY1 = "gate_energy1"
CONF_GATE_ENERGY2 = "gate_energy2"
CONF_GATE_ENERGY3 = "gate_energy3"
CONF_GATE_ENERGY4 = "gate_energy4"
CONF_GATE_ENERGY5 = "gate_energy5"
CONF_GATE_ENERGY6 = "gate_energy6"
CONF_GATE_ENERGY7 = "gate_energy7"
CONF_GATE_ENERGY8 = "gate_energy8"
CONF_GATE_ENERGY9 = "gate_energy9"
CONF_GATE_ENERGY10 = "gate_energy10"
CONF_GATE_ENERGY11 = "gate_energy11"
CONF_GATE_ENERGY12 = "gate_energy12"
CONF_GATE_ENERGY13 = "gate_energy13"
CONF_GATE_ENERGY14 = "gate_energy14"
CONF_GATE_ENERGY15 = "gate_energy15"
CONF_GATE_ENERGY16 = "gate_energy16"
CONF_GATES = [
    CONF_GATE_ENERGY1,
    CONF_GATE_ENERGY2,
    CONF_GATE_ENERGY3,
    CONF_GATE_ENERGY4,
    CONF_GATE_ENERGY5,
    CONF_GATE_ENERGY6,
    CONF_GATE_ENERGY7,
    CONF_GATE_ENERGY8,
    CONF_GATE_ENERGY9,
    CONF_GATE_ENERGY10,
    CONF_GATE_ENERGY11,
    CONF_GATE_ENERGY12,
    CONF_GATE_ENERGY13,
    CONF_GATE_ENERGY14,
    CONF_GATE_ENERGY15,
    CONF_GATE_ENERGY16,
]

CONFIG_SCHEMA = cv.All(
    cv.COMPONENT_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(LD2420Sensor),
            cv.GenerateID(CONF_LD2420_ID): cv.use_id(LD2420Component),
            cv.Optional(CONF_MOVING_DISTANCE): sensor.sensor_schema(
                device_class=DEVICE_CLASS_DISTANCE, unit_of_measurement=UNIT_CENTIMETER
            ),
            cv.Optional(CONF_GATE_ENERGY1): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY2): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY3): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY4): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY5): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY6): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY7): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY8): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY9): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY10): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY11): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY12): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY13): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY14): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY15): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
            cv.Optional(CONF_GATE_ENERGY16): sensor.sensor_schema(
                device_class=DEVICE_CLASS_ENERGY, unit_of_measurement=UNIT_WATT
            ),
        }
    ),
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    if CONF_MOVING_DISTANCE in config:
        sens = await sensor.new_sensor(config[CONF_MOVING_DISTANCE])
        cg.add(var.set_distance_sensor(sens))
    for idx,CONF_GATE_ENERGY in enumerate(CONF_GATES):
        if CONF_GATE_ENERGY in config:
            sens = await sensor.new_sensor(config[CONF_GATE_ENERGY])
            cg.add(var.set_energy_sensor(sens,idx))
    ld2420 = await cg.get_variable(config[CONF_LD2420_ID])
    cg.add(ld2420.register_listener(var))
