package com.distributed.registerservice.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Data
@Table(name = "users") 
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String email;
    private String password;
}
