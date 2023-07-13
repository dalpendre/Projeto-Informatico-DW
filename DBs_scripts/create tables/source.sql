create table t_road_event
(
    road_event_key serial
        primary key,
    description    varchar(100) not null,
    severity       varchar(10)  not null,
    status         varchar(11)  not null,
    impact_level   varchar(11)  not null
);

alter table t_road_event
    owner to postgres;

create table t_road_sign
(
    road_sign_key         integer     not null
        primary key,
    road_sign_description varchar(50) not null,
    road_sign_code        varchar(10) not null,
    road_sign_symbol      bytea       not null,
    road_sign_class       varchar(20) not null,
    road_sign_visibility  varchar(20) not null
);

alter table t_road_sign
    owner to postgres;

create table t_event
(
    event_key             serial
        primary key,
    designation           varchar(100)     not null,
    start_time            double precision not null,
    end_time              double precision not null,
    flag_single_day_event boolean          not null
);

alter table t_event
    owner to postgres;

create table t_zone
(
    zone_key         serial
        primary key,
    zone_name        varchar(100) not null,
    zone_type        varchar(30)  not null,
    zone_description varchar(30)  not null,
    zone_area        varchar(30)  not null
);

alter table t_zone
    owner to postgres;

create table t_road
(
    road_key        serial
        primary key,
    road_name       varchar(20)      not null,
    road_type       varchar(50)      not null,
    road_length     bigint           not null,
    number_of_lanes smallint         not null,
    start_point     double precision not null,
    end_point       double precision not null
);

alter table t_road
    owner to postgres;

create table t_segment
(
    segment_key     serial
        primary key,
    road_key        bigint           not null
        references t_road,
    segment_name    varchar(20)      not null,
    segment_type    varchar(20)      not null,
    segment_length  bigint           not null,
    number_of_lanes smallint         not null,
    start_point     double precision not null,
    end_point       double precision not null
);

alter table t_segment
    owner to postgres;

create table t_time
(
    time_key              serial
        primary key,
    event_key             integer     not null
        references t_event,
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

alter table t_time
    owner to postgres;

create table t_cam
(
    cam_key          serial
        primary key,
    time_key         bigint           not null
        references t_time,
    segment_key      bigint           not null
        references t_segment,
    station_id       bigint           not null,
    latitude         double precision not null,
    longitude        double precision not null,
    altitude         integer          not null,
    speed            integer          not null,
    heading          integer          not null,
    acceleration     integer          not null,
    station_type     integer          not null,
    vehicle_role     integer          not null,
    time_stamp       bigint           not null,
    fuel_type        varchar(3)       not null,
    activation_data  varchar(3)       not null,
    stationary_since integer
);

alter table t_cam
    owner to postgres;

create table t_ivim
(
    ivim_key      serial
        primary key,
    road_sign_key integer not null
        references t_road_sign,
    zone_key      integer not null
        references t_zone,
    latitude      integer not null,
    longitude     integer not null,
    altitude      integer not null
);

alter table t_ivim
    owner to postgres;

create table t_denm
(
    denm_key                                                      serial
        primary key,
    time_key                                                      integer not null
        references t_time,
    road_event_key                                                integer not null
        references t_road_event,
    time_stamp                                                    bigint  not null,
    latitude                                                      bigint  not null,
    longitude                                                     bigint  not null,
    altitude                                                      bigint  not null,
    heading                                                       integer not null,
    cause                                                         integer not null,
    traffic_sub_cause                                             integer,
    road_works_sub_cause                                          integer,
    accident_sub_cause                                            integer,
    slow_vehicle_sub_cause                                        integer,
    stationary_vehicle_sub_cause                                  integer,
    human_problem_sub_cause                                       integer,
    collision_risk_sub_cause                                      integer,
    dangerous_situation_sub_cause                                 integer,
    vehicle_break_down_sub_cause                                  integer,
    post_crash_sub_cause                                          integer,
    human_presence_on_the_road_sub_cause                          integer,
    adverse_weather_condition_extreme_weather_condition_sub_cause integer,
    adverse_weather_condition_adhesion_sub_cause                  integer,
    adverse_weather_condition_visibility_sub_cause                integer,
    adverse_weather_condition_precipitation_sub_cause             integer,
    emergency_vehicle_approaching_sub_cause                       integer,
    hazardous_location_dangerous_curve_sub_cause                  integer,
    hazardous_location_surface_condition_sub_cause                integer,
    hazardous_location_obstacle_on_the_road_sub_cause             integer,
    hazardous_location_animal_on_the_road_sub_cause               integer,
    rescue_and_recovery_work_in_progress_sub_cause                integer,
    dangerous_end_of_queue_sub_cause                              integer,
    signal_violation_sub_cause                                    integer,
    wrong_way_driving_sub_cause                                   integer
);

alter table t_denm
    owner to postgres;

