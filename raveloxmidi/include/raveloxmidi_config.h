#ifndef _RAVELOXMIDI_CONFIG_H
#define _RAVELOXMIDI_CONFIG_H

#include "kv_table.h"

void config_init( int argc, char *argv[] );
void config_teardown( void );

char *config_string_get( char *key );
int config_int_get( char *key );
long config_long_get( char *key );
int config_is_set( char *key );

void config_add_item(char *key, char *value);
void config_dump( void );

void config_usage( void );

#define MAX_CONFIG_LINE	1024

#endif
