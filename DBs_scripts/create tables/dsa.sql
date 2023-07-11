create table t_data_road_event
(
    road_event_key serial
        primary key,
    description    varchar(100) not null,
    severity       varchar(15)  not null,
    status         varchar(15)  not null,
    impact_level   varchar(11)  not null
);

alter table t_data_road_event
    owner to postgres;

create table t_data_road_sign
(
    road_sign_key         serial
        primary key,
    road_sign_description varchar(50) not null,
    road_sign_code        varchar(10) not null,
    road_sign_symbol      bytea       not null,
    road_sign_class       varchar(20) not null,
    road_sign_visibility  varchar(20) not null
);

alter table t_data_road_sign
    owner to postgres;

create table t_data_event
(
    event_key             serial
        primary key,
    designation           varchar(100)     not null,
    start_time            double precision not null,
    end_time              double precision not null,
    flag_single_day_event boolean          not null
);

alter table t_data_event
    owner to postgres;

create table t_data_zone
(
    zone_key         serial
        primary key,
    zone_name        varchar(100) not null,
    zone_type        varchar(50)  not null,
    zone_description varchar(50)  not null,
    zone_area        varchar(50)  not null
);

alter table t_data_zone
    owner to postgres;

create table t_data_road
(
    road_key        serial
        primary key,
    road_name       varchar(20)      not null,
    road_type       varchar(50)      not null,
    road_length     bigint           not null,
    number_of_lanes bigint           not null,
    start_point     double precision not null,
    end_point       double precision not null
);

alter table t_data_road
    owner to postgres;

create table t_data_segment
(
    segment_key     serial
        primary key,
    road_key        integer          not null
        references t_data_road,
    segment_name    varchar(20)      not null,
    segment_type    varchar(20)      not null,
    segment_length  integer          not null,
    number_of_lanes integer          not null,
    start_point     double precision not null,
    end_point       double precision not null
);

alter table t_data_segment
    owner to postgres;

create table t_data_time
(
    time_key              serial
        primary key,
    event_key             integer     not null
        references t_data_event,
    c_day                 integer     not null,
    c_month               integer     not null,
    c_year                integer     not null,
    weekend_day           boolean     not null,
    week_day_number       integer     not null,
    week_day_name         varchar(10) not null,
    is_holiday            boolean     not null,
    trimester             integer     not null,
    semester              integer     not null,
    season                varchar(50) not null,
    full_date_description varchar(50) not null
);

alter table t_data_time
    owner to postgres;

create table t_data_denm
(
    denm_key                                                      serial
        primary key,
    time_key                                                      integer     not null
        references t_data_time,
    road_event_key                                                integer     not null
        references t_data_road_event,
    time_stamp                                                    bigint      not null,
    latitude                                                      integer     not null,
    longitude                                                     integer     not null,
    altitude                                                      bigint      not null,
    heading                                                       integer     not null,
    cause                                                         varchar(50) not null,
    traffic_cause                                                 varchar(50),
    road_works_sub_cause                                          varchar(50),
    accident_sub_cause                                            varchar(50),
    slow_vehicle_sub_cause                                        varchar(50),
    stationary_vehicle_sub_cause                                  varchar(50),
    human_problem_sub_cause                                       varchar(50),
    collision_risk_sub_cause                                      varchar(50),
    dangerous_situation_sub_cause                                 varchar(50),
    vehicle_break_down_sub_cause                                  varchar(50),
    post_crash_sub_cause                                          varchar(50),
    human_presence_on_the_road_sub_cause                          varchar(50),
    adverse_weather_condition_extreme_weather_condition_sub_cause varchar(50),
    adverse_weather_condition_adhesion_sub_cause                  varchar(50),
    adverse_weather_condition_visibility_sub_cause                varchar(50),
    adverse_weather_condition_precipitation_sub_cause             varchar(50),
    emergency_vehicle_approaching_sub_cause                       varchar(50),
    hazardous_location_surface_condition_sub_cause                varchar(50),
    hazardous_location_obstacle_on_the_road_sub_cause             varchar(50),
    hazardous_location_animal_on_the_road_sub_cause               varchar(50),
    rescue_and_recovery_work_in_progress_sub_cause                varchar(50),
    dangerous_end_of_queue_sub_cause                              varchar(50),
    hazardous_location_dangerous_curve_sub_cause                  varchar(50),
    signal_violation_sub_cause                                    varchar(50),
    wrong_way_driving_sub_cause                                   varchar(50)
);

alter table t_data_denm
    owner to postgres;

create table t_data_ivim
(
    ivim_key      serial
        primary key,
    road_sign_key integer not null
        references t_data_road_sign,
    zone_key      integer not null
        references t_data_zone,
    latitude      integer not null,
    longitude     integer not null,
    altitude      integer not null
);

alter table t_data_ivim
    owner to postgres;

create table t_data_cam
(
    cam_key                   serial
        primary key,
    time_key                  bigint      not null
        references t_data_time,
    segment_key               bigint      not null
        references t_data_segment,
    station_id                bigint      not null,
    latitude                  integer     not null,
    longitude                 integer     not null,
    altitude                  integer     not null,
    speed                     integer     not null,
    heading                   integer     not null,
    acceleration              integer     not null,
    station_type              varchar(30) not null,
    vehicle_role              varchar(30) not null,
    time_stamp                bigint      not null,
    fuel_type                 varchar(20) not null,
    brake_pedal_engaged       boolean     not null,
    gas_pedal_engaged         boolean     not null,
    emergency_pedal_engaged   boolean     not null,
    collision_warning_engaged boolean     not null,
    acc_engaged               boolean     not null,
    cruise_control_engaged    boolean     not null,
    speed_limiter_engaged     boolean     not null,
    stationary_since          varchar(30)
);

alter table t_data_cam
    owner to postgres;

create table t_clean_road_event
(
    road_event_key serial
        primary key,
    description    varchar(100) not null,
    severity       varchar(15)  not null,
    status         varchar(15)  not null,
    impact_level   varchar(11)  not null
);

alter table t_clean_road_event
    owner to postgres;

create table t_clean_road_sign
(
    road_sign_key         serial
        primary key,
    road_sign_description varchar(50) not null,
    road_sign_code        varchar(10) not null,
    road_sign_symbol      bytea       not null,
    road_sign_class       varchar(20) not null,
    road_sign_visibility  varchar(20) not null
);

alter table t_clean_road_sign
    owner to postgres;

create table t_clean_event
(
    event_key             serial
        primary key,
    designation           varchar(100)     not null,
    start_time            double precision not null,
    end_time              double precision not null,
    flag_single_day_event boolean          not null
);

alter table t_clean_event
    owner to postgres;

create table t_clean_zone
(
    zone_key         serial
        primary key,
    zone_name        varchar(100) not null,
    zone_type        varchar(50)  not null,
    zone_description varchar(50)  not null,
    zone_area        varchar(50)  not null
);

alter table t_clean_zone
    owner to postgres;

create table t_clean_road
(
    road_key        serial
        primary key,
    road_name       varchar(20)      not null,
    road_type       varchar(50)      not null,
    road_length     bigint           not null,
    number_of_lanes bigint           not null,
    start_point     double precision not null,
    end_point       double precision not null
);

alter table t_clean_road
    owner to postgres;

create table t_clean_segment
(
    segment_key     serial
        primary key,
    road_key        integer          not null
        references t_clean_road,
    segment_name    varchar(20)      not null,
    segment_type    varchar(20)      not null,
    segment_length  integer          not null,
    number_of_lanes integer          not null,
    start_point     double precision not null,
    end_point       double precision not null
);

alter table t_clean_segment
    owner to postgres;

create table t_clean_time
(
    time_key              serial
        primary key,
    event_key             integer     not null
        references t_clean_event,
    c_day                 integer     not null,
    c_month               integer     not null,
    c_year                integer     not null,
    weekend_day           boolean     not null,
    week_day_number       integer     not null,
    week_day_name         varchar(10) not null,
    is_holiday            boolean     not null,
    trimester             integer     not null,
    semester              integer     not null,
    season                varchar(50) not null,
    full_date_description varchar(50) not null
);

alter table t_clean_time
    owner to postgres;

create table t_clean_denm
(
    denm_key                                                      serial
        primary key,
    time_key                                                      integer     not null
        references t_clean_time,
    road_event_key                                                integer     not null
        references t_clean_road_event,
    time_stamp                                                    bigint      not null,
    latitude                                                      bigint      not null,
    longitude                                                     bigint      not null,
    altitude                                                      bigint      not null,
    heading                                                       integer     not null,
    cause                                                         varchar(50) not null,
    traffic_cause                                                 varchar(50),
    road_works_sub_cause                                          varchar(50),
    accident_sub_cause                                            varchar(50),
    slow_vehicle_sub_cause                                        varchar(50),
    stationary_vehicle_cause                                      varchar(50),
    human_problem_sub_cause                                       varchar(50),
    collision_risk_sub_cause                                      varchar(50),
    dangerous_situation_sub_cause                                 varchar(50),
    vehicle_break_down_sub_cause                                  varchar(50),
    post_crash_sub_cause                                          varchar(50),
    human_presence_on_the_road_sub_cause                          varchar(50),
    adverse_weather_condition_extreme_weather_condition_sub_cause varchar(50),
    adverse_weather_condition_adhesion_sub_cause                  varchar(50),
    adverse_weather_condition_visibility_sub_cause                varchar(50),
    adverse_weather_condition_precipitation_sub_cause             varchar(50),
    emergency_vehicle_approaching_sub_cause                       varchar(50),
    hazardous_location_surface_condition_sub_cause                varchar(50),
    hazardous_location_obstacle_on_the_road_sub_cause             varchar(50),
    hazardous_location_animal_on_the_road_sub_cause               varchar(50),
    rescue_and_recovery_work_in_progress_sub_cause                varchar(50),
    dangerous_end_of_queue_sub_cause                              varchar(50),
    hazardous_location_dangerous_curve_sub_cause                  varchar(50),
    signal_violation_sub_cause                                    varchar(50),
    wrong_way_driving_sub_cause                                   varchar(50)
);

alter table t_clean_denm
    owner to postgres;

create table t_clean_ivim
(
    ivim_key      serial
        primary key,
    road_sign_key integer not null
        references t_clean_road_sign,
    zone_key      integer not null
        references t_clean_zone,
    latitude      integer not null,
    longitude     integer not null,
    altitude      integer not null
);

alter table t_clean_ivim
    owner to postgres;

create table t_clean_cam
(
    cam_key                   serial
        primary key,
    time_key                  bigint      not null
        references t_clean_time,
    segment_key               bigint      not null
        references t_clean_segment,
    station_id                bigint      not null,
    latitude                  integer     not null,
    longitude                 integer     not null,
    altitude                  integer     not null,
    speed                     integer     not null,
    heading                   integer     not null,
    acceleration              integer     not null,
    station_type              varchar(30) not null,
    vehicle_role              varchar(30) not null,
    time_stamp                bigint      not null,
    fuel_type                 varchar(20) not null,
    brake_pedal_engaged       boolean     not null,
    gas_pedal_engaged         boolean     not null,
    emergency_pedal_engaged   boolean     not null,
    collision_warning_engaged boolean     not null,
    acc_engaged               boolean     not null,
    cruise_control_engaged    boolean     not null,
    speed_limiter_engaged     boolean     not null,
    stationary_since          varchar(30)
);

alter table t_clean_cam
    owner to postgres;

